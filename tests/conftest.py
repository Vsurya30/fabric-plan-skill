import sys
from pathlib import Path

# The runtime lives under scripts/; make `import runtime` work for pytest.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
