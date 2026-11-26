"""IBCS recipe charts: native template selectors plus bucket bindings the template accepts."""
import unittest
from pathlib import Path
from runtime.chart_filters import audit_chart_filters
from runtime.codec import load
from runtime.ibcs_charts import RECIPES, TEMPLATES, describe, recipe_chart, recipes, required_buckets
from runtime.identity import Registry
from runtime.intelligence import chart, column_chart

ROOT = Path(__file__).resolve().parents[1]
VALUES = {'AC': 'Metrics[Units]', 'PY': 'Metrics[Price]', 'PL': 'Metrics[Cost]', 'FC': 'Metrics[Expense]'}


def model():
    return load(ROOT / 'fixtures/model.json')


def spec(code, *buckets, **extra):
    measures = {b: VALUES[b] for b in buckets if b in VALUES}
    out = {'label': code + ' chart', 'recipe': code, 'category': 'Region[Region]', 'measures': measures}
    if 'stack' in buckets:
        out['stack'] = 'Product[Product]'
    out.update(extra)
    return out


def buckets(p):
    return [(a['id'], a['bucketId']) for a in p['pivotAssignments']]


class RecipeCharts(unittest.TestCase):
    def build(self, s):
        return recipe_chart(model(), s, Registry())

    def test_every_recipe_builds_with_its_required_bindings(self):
        for code, (name, types, _) in RECIPES.items():
            with self.subTest(code=code):
                required = required_buckets(code)
                p = self.build(spec(code, *required))
                self.assertEqual(p['visualType'], 50)
                self.assertEqual(p['chartType'], types[0])
                self.assertEqual(p['visualState']['chartType'], types[0])
                self.assertEqual(sorted(b for _, b in buckets(p)), sorted(required))
                audit_chart_filters(p)
                self.assertTrue(describe(p)['selectorsAgree'])

    def test_c01_binds_category_stack_and_three_measures(self):
        p = self.build(spec('C01', 'axis', 'AC', 'PL', 'FC', 'stack'))
        self.assertEqual(buckets(p), [('Region[Region]', 'axis'), ('Product[Product]', 'stack'),
                                      ('Metrics[Units]', 'AC'), ('Metrics[Cost]', 'PL'), ('Metrics[Expense]', 'FC')])
        roles = {a['bucketId']: a['dataRoleType'] for a in p['pivotAssignments']}
        self.assertEqual(roles, {'axis': 'Grouping', 'stack': 'Grouping', 'AC': 'Measure', 'PL': 'Measure', 'FC': 'Measure'})

    def test_missing_recipe_binding_is_named(self):
        with self.assertRaisesRegex(ValueError, r'C01 .*needs bindings for FC'):
            self.build(spec('C01', 'AC', 'PL', 'stack'))
        with self.assertRaisesRegex(ValueError, r'C02 .*stack'):
            self.build(spec('C02', 'AC'))

    def test_unknown_recipe_and_template_are_refused(self):
        with self.assertRaisesRegex(ValueError, 'no C11'):
            self.build(spec('C11', 'AC'))
        s = spec('C03', 'AC', 'PY', 'FC')
        del s['recipe']
        s['chartType'] = 'PIE_CHART'
        with self.assertRaisesRegex(ValueError, 'Unsupported chart template'):
            self.build(s)

    def test_recipe_chart_type_must_be_one_the_recipe_names(self):
        with self.assertRaisesRegex(ValueError, 'C03 uses chartType COLUMN_VERTICAL'):
            self.build(spec('C03', 'AC', 'PY', 'FC', chartType='LINE'))

    def test_c08_mixed_variant_uses_area_with_several_actuals(self):
        s = spec('C08', 'AC', chartType='AREA')
        s['measures']['AC'] = [{'field': 'Metrics[Units]', 'label': 'Direct'}, {'field': 'Metrics[Hours]', 'label': 'Retail'}]
        p = self.build(s)
        self.assertEqual(p['chartType'], 'AREA')
        actuals = [a for a in p['pivotAssignments'] if a['bucketId'] == 'AC']
        self.assertEqual([(a['order'], a['customName']) for a in actuals], [(0, 'Direct'), (1, 'Retail')])

    def test_native_stacked_area_needs_a_stack(self):
        with self.assertRaisesRegex(ValueError, 'STACKED_AREA needs a stack'):
            self.build(spec('C08', 'AC'))

    def test_stacked_template_without_stack_needs_two_measures(self):
        s = {'label': 'Stacked', 'chartType': 'STACKED_COLUMN_VERTICAL', 'category': 'Region[Region]',
             'measures': {'AC': VALUES['AC']}}
        with self.assertRaisesRegex(ValueError, 'renders as COLUMN_VERTICAL'):
            self.build(s)
        s['measures']['PY'] = VALUES['PY']
        self.assertEqual(self.build(s)['chartType'], 'STACKED_COLUMN_VERTICAL')

    def test_percentage_stacked_templates_are_available_without_a_recipe(self):
        for chart_type in ('PERCENTAGE_STACKED_VERTICAL', 'PERCENTAGE_STACKED_HORIZONTAL'):
            s = {'label': '100%', 'chartType': chart_type, 'category': 'Region[Region]',
                 'stack': 'Product[Product]', 'measures': {'AC': VALUES['AC']}}
            self.assertEqual(self.build(s)['visualState']['chartType'], chart_type)

    def test_bucket_limits_follow_the_template(self):
        s = spec('C03', 'AC', 'PY', 'FC')
        s['measures']['AC'] = [VALUES['AC'], 'Metrics[Hours]']
        with self.assertRaisesRegex(ValueError, 'at most 1 measure'):
            self.build(s)
        with self.assertRaisesRegex(ValueError, 'has no stack bucket'):
            self.build(spec('C03', 'AC', 'PY', 'FC', stack='Product[Product]'))
        with self.assertRaisesRegex(ValueError, 'has no measure bucket FC'):
            self.build({'label': 'Scatter', 'recipe': 'C09', 'category': 'Region[Region]',
                        'measures': {'AC': VALUES['AC'], 'PY': VALUES['PY'], 'FC': VALUES['FC']}})

    def test_comparison_templates_need_two_measures(self):
        s = {'label': 'Bridge', 'chartType': 'COLUMN_WATERFALL_VERTICAL', 'category': 'Region[Region]',
             'measures': {'AC': VALUES['AC']}}
        with self.assertRaisesRegex(ValueError, 'at least 2 measures'):
            self.build(s)
        with self.assertRaisesRegex(ValueError, 'BUBBLE_PLOT needs 1 measure in bucket PL'):
            self.build({'label': 'Bubble', 'chartType': 'BUBBLE_PLOT', 'category': 'Region[Region]',
                        'measures': {'AC': VALUES['AC'], 'PY': VALUES['PY']}})

    def test_bindings_keep_dimension_and_measure_roles(self):
        with self.assertRaisesRegex(ValueError, 'Semantic measures belong in Values'):
            self.build(spec('C03', 'AC', 'PY', 'FC', category='Metrics[Hours]'))
        with self.assertRaisesRegex(ValueError, 'different fields'):
            self.build(spec('C02', 'AC', 'stack', stack='Region[Region]'))
        s = spec('C03', 'AC', 'PY', 'FC')
        s['measures']['PY'] = VALUES['AC']
        with self.assertRaisesRegex(ValueError, 'same value is bound to AC and PY'):
            self.build(s)

    def test_unconsumed_options_are_refused(self):
        with self.assertRaisesRegex(ValueError, 'Unconsumed chart options: theme'):
            self.build(spec('C03', 'AC', 'PY', 'FC', theme='ibcs'))
        s = spec('C03', 'AC', 'PY', 'FC')
        s['measures']['AC'] = {'field': VALUES['AC'], 'color': '#000000'}
        with self.assertRaisesRegex(ValueError, 'Unconsumed measure options in AC: color'):
            self.build(s)

    def test_catalog_lists_every_recipe_with_a_supported_template(self):
        catalog = recipes()
        self.assertEqual(sorted(catalog), sorted(RECIPES))
        for entry in catalog.values():
            self.assertTrue(set(entry['chartTypes']) <= set(TEMPLATES))
        self.assertEqual(catalog['C08']['requiredBuckets'], {'STACKED_AREA': ['axis', 'AC', 'stack'],
                                                             'AREA': ['axis', 'AC']})
        self.assertEqual(catalog['C10']['requiredBuckets']['BUBBLE_PLOT'], ['axis', 'AC', 'PY', 'PL'])


class RecipeGuide(unittest.TestCase):
    def test_guide_table_matches_the_recipe_catalog(self):
        import re
        text = (ROOT / 'references/ibcs-charts.md').read_text(encoding='utf-8')
        rows = re.findall(r'^\| (C\d\d) \| ([^|]+) \| `([A-Z_]+)`', text, re.M)
        self.assertEqual({code: (name.strip(), chart_type) for code, name, chart_type in rows},
                         {code: (name, types[0]) for code, (name, types, _) in RECIPES.items()})

    def test_ibcs_and_stacked_requests_route_to_the_guide(self):
        from runtime.discovery import discover
        for query in ('stacked charts', 'IBCS C01 stacked column', 'waterfall chart'):
            self.assertEqual(discover(query)['modules'][0]['id'], 'IBCS-CHARTS', query)


class DashboardCharts(unittest.TestCase):
    def test_plain_column_chart_selects_its_template(self):
        p = column_chart(model(), {'category': 'Region[Region]', 'field': 'Metrics[Units]', 'label': 'Units'}, Registry())
        self.assertEqual((p['chartType'], p['visualState']['chartType']), ('COLUMN_VERTICAL', 'COLUMN_VERTICAL'))
        self.assertEqual(buckets(p), [('Region[Region]', 'axis'), ('Metrics[Units]', 'AC')])

    def test_variance_chart_keeps_both_selectors_on_the_integrated_template(self):
        p = column_chart(model(), {'category': 'Region[Region]', 'field': 'Metrics[Units]',
                                   'comparisonField': 'Metrics[Price]', 'label': 'Units vs price'}, Registry())
        self.assertEqual((p['chartType'], p['visualState']['chartType']),
                         ('COLUMN_INTEGRATED_VERTICAL', 'COLUMN_INTEGRATED_VERTICAL'))

    def test_dispatcher_routes_recipe_specs(self):
        p = chart(model(), spec('C04', 'AC', 'PL'), Registry())
        self.assertEqual(p['chartType'], 'COLUMN_HORIZONTAL')
        p = chart(model(), {'category': 'Region[Region]', 'field': 'Metrics[Units]', 'label': 'Units'}, Registry())
        self.assertEqual(p['chartType'], 'COLUMN_VERTICAL')

    def test_generated_dashboard_carries_recipe_charts(self):
        from runtime.planning_presentation import build_application
        s = {'name': 'IBCS review', 'sheets': [{'name': 'Units', 'rows': ['Region[Region]'], 'columns': ['Period[Month]'],
              'measures': [{'key': 'units', 'label': 'Units', 'kind': 'Native', 'source': 'Metrics[Units]'}]}],
             'dashboards': [{'name': 'Review', 'owner': 'Units', 'slicers': [{'field': 'Region[Region]'}], 'cards': [],
                             'charts': [spec('C01', 'AC', 'PL', 'FC', 'stack'), spec('C04', 'AC', 'PL')]}]}
        result = build_application(model(), s)
        charts = [o['properties'] for o in result['raw'].values()
                  if o.get('properties', {}).get('chartType') in TEMPLATES]
        self.assertEqual(sorted(p['chartType'] for p in charts), ['COLUMN_HORIZONTAL', 'STACKED_COLUMN_VERTICAL'])
        for p in charts:
            self.assertEqual(p['visualState']['chartType'], p['chartType'])
            audit_chart_filters(p)


if __name__ == '__main__':
    unittest.main()
