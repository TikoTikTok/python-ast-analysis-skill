import ast

from .base import Rule, dotted_name

WEAK = {"hashlib.md5", "hashlib.sha1"}


class WeakHashRule(Rule):
    rule_id = "PY003"
    severity = "medium"
    description = "Weak hash algorithm (md5/sha1)"

    def check(self, tree, path, lines):
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = dotted_name(node.func)
                if name in WEAK:
                    yield self.make(
                        node, path, lines,
                        f"{name} is a weak hash; use sha256 or stronger",
                        name,
                    )
