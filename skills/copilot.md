# Copilot skill: pyast-skill

- Run tests: `pytest -q`. Run analyzer on itself: `pyast-skill scan src --json`.
- When adding or changing a rule, follow `shared-rule-authoring.md` and add a positive test.
- Keep analysis AST-only (stdlib `ast`); no third-party runtime dependencies.
- Keep the README rule catalog in sync with `all_rules()`.
