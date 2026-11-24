"""Validated, opt-in adapter contracts for PowerTable Approvals and Forms.

These are workload-service routes, not public Fabric REST endpoints. A caller
must supply an explicitly approved environment profile and current runtime
source/column identities.
"""
import base64
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from .codec import dumps, load, save, sha


IDENTIFIER = re.compile(r"[A-Za-z0-9_. -]+")
OPAQUE_ID = re.compile(r"[A-Za-z0-9_.:@=-]+")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _identifier(value, label):
    if not isinstance(value, str) or not value or not IDENTIFIER.fullmatch(value):
        raise ValueError("Invalid PowerTable "+label)
    return value


def _opaque_id(value, label):
    if not isinstance(value, (str, int)) or isinstance(value, bool):
        raise ValueError("PowerTable "+label+" must be a runtime scalar identity")
    value = str(value)
    if not value or not OPAQUE_ID.fullmatch(value):
        raise ValueError("Invalid PowerTable "+label)
    return value


def source_path(schema, table, *, source_id=None, suffix=None):
    if source_id is not None:
        if suffix not in ("approvals", "forms"):
            raise ValueError("PowerTable source suffix must be approvals or forms")
        source = _opaque_id(source_id, "sourceId")
        return f"/v2/powertable/sources/{source}/{suffix}/"
    schema = _identifier(schema, "schema")
    table = _identifier(table, "table")
    path = f"/v2/powertable/sources/{schema}/{table}/"
    if suffix is not None:
        raise ValueError("Source resolution does not accept a suffix")
    return path


def approval_payload(approvers, *, rule_type=10, multi_level_enabled=0, approval_level=1):
    if rule_type not in (10, 20, 30):
        raise ValueError("Approval rule type must be 10 (default), 20 (manual), or 30 (lookup)")
    if multi_level_enabled != 0:
        raise ValueError("This adapter currently supports single-level approval assignment")
    if approval_level not in (1, 2, 3):
        raise ValueError("Approval level must be 1, 2, or 3")
    if not isinstance(approvers, list) or not approvers:
        raise ValueError("At least one resolved approver is required")
    entity_types = {"USER": 10, "GROUP": 20}
    normalized = []
    seen = set()
    for approver in approvers:
        if not isinstance(approver, dict):
            raise ValueError("Approver entries must be objects")
        graph_id = approver.get("graphId")
        entity_type = approver.get("entityType")
        if not isinstance(graph_id, str) or not graph_id:
            raise ValueError("Approver graphId is required")
        if entity_type in entity_types:
            entity_type = entity_types[entity_type]
        if entity_type not in (10, 20):
            raise ValueError("Approver entityType must be USER/GROUP or 10/20")
        if graph_id in seen:
            raise ValueError("Duplicate approver graphId")
        seen.add(graph_id)
        item = {"graphId": graph_id, "entityType": entity_type}
        if "level" in approver:
            if approver["level"] not in (1, 2, 3):
                raise ValueError("Approver level must be 1, 2, or 3")
            item["level"] = approver["level"]
        normalized.append(item)
    return {
        "ruleType": rule_type,
        "defaultApprovers": {"addedApproverObjs": normalized},
        "multiLevelEnabled": multi_level_enabled,
        "approvalLevel": approval_level,
    }


def form_payload(title, fields, *, description="", restrict_multiple_entry=1,
                 config=None, layout_meta=None, logo=None):
    if not isinstance(title, str) or not title.strip() or len(title) > 255:
        raise ValueError("Form title must contain 1-255 characters")
    if description is None:
        description = ""
    if not isinstance(description, str) or len(description) > 255:
        raise ValueError("Form description must contain at most 255 characters")
    if restrict_multiple_entry not in (0, 1):
        raise ValueError("restrict_multiple_entry must be 0 or 1")
    if not isinstance(fields, list) or not fields:
        raise ValueError("At least one form field is required")
    normalized = []
    for field in fields:
        if not isinstance(field, dict):
            raise ValueError("Form fields must be objects")
        column_id = _opaque_id(field.get("columnConfigId"), "columnConfigId")
        mandatory = field.get("mandatory", 0)
        if mandatory not in (0, 1):
            raise ValueError("Form field mandatory must be 0 or 1")
        item = {
            "columnConfigId": column_id,
            "description": field.get("description", ""),
            "mandatory": mandatory,
            "defaultValue": field.get("defaultValue"),
        }
        if not isinstance(item["description"], str) or len(item["description"]) > 255:
            raise ValueError("Form field description must contain at most 255 characters")
        normalized.append(item)
    form = {
        "title": title.strip(),
        "description": description,
        "restrictMultipleEntry": restrict_multiple_entry,
        "logo": logo,
    }
    if config is not None:
        if not isinstance(config, dict):
            raise ValueError("Form config must be an object")
        form["config"] = config
    if layout_meta is not None:
        if not isinstance(layout_meta, dict):
            raise ValueError("Form layoutMeta must be an object")
        form["layoutMeta"] = layout_meta
    return {"formConfiguration": form, "fieldsConfiguration": normalized}


class PowerTableServiceClient:
    def __init__(self, base, token_environment, allowed_hosts, *, run, auth_scheme="Bearer",
                 context_headers=None, adapter=None, authorized_mutation=False):
        if not isinstance(allowed_hosts, list) or not allowed_hosts:
            raise ValueError("approved external adapter requires explicit allowedHosts")
        parsed = urllib.parse.urlsplit(base)
        if (parsed.scheme != "https" or not parsed.hostname or parsed.username
                or parsed.password or parsed.query or parsed.fragment
                or parsed.hostname not in allowed_hosts):
            raise ValueError("Unapproved PowerTable service endpoint")
        if auth_scheme not in ("Bearer", "MWCToken"):
            raise ValueError("PowerTable authScheme must be Bearer or MWCToken")
        self.base = base.rstrip("/")
        self.token_environment = token_environment
        self.allowed_hosts = set(allowed_hosts)
        self.auth_scheme = auth_scheme
        self.context_headers = dict(context_headers or {})
        self.authorized_mutation = authorized_mutation is True
        if any(key.casefold() in ("authorization", "cookie") for key in self.context_headers):
            raise ValueError("Credentials must come from the process environment")
        self.adapter = adapter or self._http
        self.run = Path(run)
        self.run.mkdir(parents=True, exist_ok=True)

    def check_route(self, route):
        target = route if route.startswith("https://") else self.base + "/" + route.lstrip("/")
        parsed = urllib.parse.urlsplit(target)
        if (parsed.scheme != "https" or parsed.hostname not in self.allowed_hosts
                or parsed.username or parsed.password or parsed.fragment
                or "/v2/powertable/" not in parsed.path):
            raise ValueError("Route is outside the approved PowerTable service surface")
        return target

    def _http(self, method, url, headers, body):
        request = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            response = urllib.request.build_opener(NoRedirect).open(request, timeout=70)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            raw = response.read(64 * 1024 * 1024 + 1)
            if len(raw) > 64 * 1024 * 1024:
                raise ValueError("PowerTable response exceeds 64 MiB")
            try:
                body_value = json.loads(raw.decode()) if raw else None
            except (ValueError, UnicodeDecodeError):
                body_value = {"binaryBase64": base64.b64encode(raw).decode()}
            return {"status": response.status, "headers": dict(response.headers), "body": body_value}

    def request(self, method, route, body=None, *, label):
        method = method.upper()
        if method not in ("GET", "POST", "PATCH", "DELETE"):
            raise ValueError("Unsupported PowerTable service method")
        if method != "GET" and not self.authorized_mutation:
            raise ValueError("PowerTable service mutation requires authorizedMutation")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", label):
            raise ValueError("Unsafe operation label")
        token = os.environ.get(self.token_environment)
        if not token:
            raise ValueError("Set "+self.token_environment+" in the process environment")
        url = self.check_route(route)
        raw = None if body is None else dumps(body).encode()
        intent = {"method": method, "url": url, "bodyHash": sha(raw) if raw is not None else None}
        intent_path = self.run / (label + ".intent.json")
        response_path = self.run / (label + ".response.json")
        if intent_path.exists():
            if load(intent_path)["request"] != intent:
                raise ValueError("Journal label reused for different PowerTable request")
            if response_path.exists():
                response = load(response_path)
                if not 200 <= response["status"] < 300:
                    raise RuntimeError(f"PowerTable service HTTP {response['status']}")
                return response
            raise RuntimeError("UNCERTAIN_SUBMISSION: reconcile PowerTable service state before retry")
        headers = {
            "Authorization": self.auth_scheme + " " + token,
            "Content-Type": "application/json",
            **self.context_headers,
        }
        save(intent_path, {"request": intent})
        response = self.adapter(method, url, headers, raw)
        def redact(value):
            if isinstance(value, dict):
                return {key: "<not-persisted>" if key.casefold() in {
                    "token", "access_token", "accesstoken", "authorization",
                    "password", "client_secret", "mwctoken",
                } else redact(item) for key, item in value.items()}
            if isinstance(value, list):
                return [redact(item) for item in value]
            return value
        clean = {"status": response["status"], "body": redact(response.get("body"))}
        if not 200 <= clean["status"] < 300:
            save(response_path, clean)
            raise RuntimeError(f"PowerTable service HTTP {clean['status']}: {clean['body']}")
        save(response_path, clean)
        return clean


def client_from_config(config, run, *, adapter=None):
    if config.get("approvedExternalAdapter") is not True:
        raise ValueError("PowerTable workload service requires approvedExternalAdapter=true")
    for field in ("apiBase", "tokenEnvironment", "allowedHosts"):
        if not config.get(field):
            raise ValueError("Missing approved PowerTable service profile field: "+field)
    return PowerTableServiceClient(
        config["apiBase"], config["tokenEnvironment"], config["allowedHosts"],
        run=run, auth_scheme=config.get("authScheme", "Bearer"),
        context_headers=config.get("contextHeaders"), adapter=adapter,
        authorized_mutation=config.get("authorizedMutation") is True,
    )


def resolve_source(client, source, *, label):
    required = ("dbName", "dbHost", "schema", "table")
    if not isinstance(source, dict) or any(not source.get(key) for key in required):
        raise ValueError("Source resolution requires dbName, dbHost, schema and table")
    path = source_path(source["schema"], source["table"])
    query = {key: source[key] for key in ("dbName", "dbHost", "connectionId", "databaseVariable") if source.get(key)}
    response = client.request("GET", path + "?" + urllib.parse.urlencode(query), label=label)
    body = response.get("body") or {}
    payload = body.get("payload", body)
    if not isinstance(payload, dict) or payload.get("isConfigured") is not True or not payload.get("dataSourceId"):
        raise ValueError("PowerTable source is not configured or cannot be resolved")
    return {"sourceId": str(payload["dataSourceId"]), "visualId": payload.get("visualId"),
            "sheetName": payload.get("sheetName"), "columnConfig": payload.get("columnConfig")}


def create_approval(client, source_id, payload, *, label):
    return client.request("POST", source_path("ignored", "ignored", source_id=source_id,
                                              suffix="approvals"), payload, label=label)


def read_approval(client, source_id, *, label):
    return client.request("GET", source_path("ignored", "ignored", source_id=source_id,
                                            suffix="approvals"), label=label)


def create_form(client, source_id, payload, *, label):
    return client.request("POST", source_path("ignored", "ignored", source_id=source_id,
                                              suffix="forms"), payload, label=label)


def read_forms(client, source_id, *, label):
    return client.request("GET", source_path("ignored", "ignored", source_id=source_id,
                                            suffix="forms"), label=label)
