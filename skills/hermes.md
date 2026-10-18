# Hermes skill: pyast-skill

Use when asked to audit Python code with AST analysis.

1. Run `pyast-skill scan <path> --json`.
2. Group findings by `rule_id`; prioritize `high` severity.
3. For each finding, read `file:line` and propose a minimal fix (e.g. `ast.literal_eval`, argument lists instead of `shell=True`, sha256, parameterized SQL).
4. Treat PY004 as a heuristic (`confidence`); verify before reporting as confirmed.

Provider stub: `pyast_skill.providers.hermes.HermesProvider` (no network calls yet).
