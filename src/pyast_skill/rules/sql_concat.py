import ast

from .base import Rule

EXEC_METHODS = {"execute", "executemany"}


def _dynamic_kind(node: ast.AST) -> str | None:
    """Return a label if the expression builds a string dynamically."""
    if isinstance(node, ast.JoinedStr):
        return "f-string"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return "concatenation"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
        return "%-format"
    return None


class SqlConcatRule(Rule):
    rule_id = "PY004"
    severity = "medium"
    description = "SQL built via concatenation/f-string passed to execute()"

    def check(self, tree, path, lines):
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in EXEC_METHODS
                and node.args
            ):
                continue
            arg = node.args[0]
            kind = _dynamic_kind(arg)
            if not kind:
                continue
            # A variable-derived part is higher risk than literal-only pieces.
            has_var = any(
                isinstance(n, (ast.Name, ast.Attribute, ast.Call, ast.Subscript))
                for n in ast.walk(arg)
            )
            yield self.make(
                node, path, lines,
                f"SQL passed to {node.func.attr}() built with {kind}; use parameterized queries",
                node.func.attr,
                severity="high" if has_var else "medium",
                confidence="medium",
            )
