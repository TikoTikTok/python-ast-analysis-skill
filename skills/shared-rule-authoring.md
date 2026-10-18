# Shared rule authoring

A rule is a `Rule` subclass in `src/pyast_skill/rules/`.

```python
class MyRule(Rule):
    rule_id = "PY005"
    severity = "medium"
    description = "..."

    def check(self, tree, path, lines):
        for node in ast.walk(tree):
            if ...:
                yield self.make(node, path, lines, "message", "symbol")
```

Checklist:
- Unique `rule_id` (`PYnnn`), severity `low|medium|high`.
- Use `dotted_name()` to resolve `a.b.c` calls; avoid regex on source.
- Set `confidence` for heuristic rules.
- Register in `all_rules()`, add a positive (and ideally negative) test, update README catalog.
