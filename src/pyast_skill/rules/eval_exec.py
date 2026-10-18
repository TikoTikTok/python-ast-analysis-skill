import ast

from .base import Rule, dotted_name


class EvalExecRule(Rule):
    rule_id = "PY001"
    severity = "high"
    description = "Use of eval() or exec()"

    def check(self, tree, path, lines):
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ("eval", "exec"):
                    yield self.make(
                        node, path, lines,
                        f"Use of {node.func.id}() allows arbitrary code execution",
                        dotted_name(node.func),
                    )
