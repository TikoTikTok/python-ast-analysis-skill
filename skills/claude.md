# Claude skill: pyast-skill

Use when asked to find risky Python patterns in a repo.

1. Install: `pip install -e .`; run `pyast-skill scan . --json --min-severity medium`.
2. Parse the JSON (`count`, `findings[]`) and read each flagged line in context.
3. Report confirmed issues with a suggested patch; mark heuristic hits (PY004) as "needs review".
4. Exit code `1` means findings exist, not that the tool failed.

Provider stub: `pyast_skill.providers.claude.ClaudeProvider` (no network calls yet).
