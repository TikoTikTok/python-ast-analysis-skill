# pyast-skill

## Purpose
A small Python static analyzer built only on the standard-library `ast` module, plus assistant skill docs (Hermes, Claude, Copilot) describing how to run it and extend it.

## Quick start
```bash
pip install -e ".[dev]"
pytest -q
pyast-skill scan src
```

## CLI usage
```
pyast-skill scan PATH [--json] [--include GLOB]... [--exclude GLOB]... [--min-severity low|medium|high]
```
- `--include` / `--exclude` are repeatable fnmatch globs matched against the relative path or file name.
- Exit code `0`: no findings. `1`: findings exist.

## Rule catalog
| ID | Severity | Detects |
|----|----------|---------|
| PY001 | high | `eval()` / `exec()` |
| PY002 | high | `subprocess.*(..., shell=True)` |
| PY003 | medium | `hashlib.md5` / `hashlib.sha1` |
| PY004 | medium/high (heuristic) | SQL built by concatenation / f-string / `%` passed to `execute`/`executemany`; high when a variable is interpolated |

## JSON output example
```json
{
  "count": 1,
  "findings": [
    {
      "rule_id": "PY001",
      "severity": "high",
      "message": "Use of eval() allows arbitrary code execution",
      "file": "app.py",
      "line": 3,
      "col": 4,
      "symbol": "eval",
      "snippet": "eval(user_input)"
    }
  ]
}
```
`confidence` is included only when a rule sets it (e.g. PY004).

## How to add a rule
1. Create `src/pyast_skill/rules/my_rule.py` with a `Rule` subclass (`rule_id`, `severity`, `check()` yielding `Finding`s via `self.make`).
2. Register it in `all_rules()` in `rules/__init__.py`.
3. Add `tests/test_my_rule.py` with a positive detection case.
4. Add it to the catalog above. See `skills/shared-rule-authoring.md`.

## Provider notes
`pyast_skill.providers` defines a `Provider` interface with `Hermes` and `Claude` stubs. They return deterministic strings and make **no API calls**. Use `get_provider("hermes")`.

## CI notes
`.github/workflows/ci.yml` runs on push and PR for Python 3.11/3.12: installs `.[dev]`, runs `pytest -q`, then a non-blocking `pyast-skill scan src --json` demo.

## Skills
See `skills/` for Hermes, Claude, Copilot and shared rule-authoring guides.
