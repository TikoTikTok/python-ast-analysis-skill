import ast

from .base import Rule, dotted_name


class SubprocessShellRule(Rule):
    rule_id = "PY002"
    severity = "high"
    description = "subprocess call with shell=True"

    def check(self, tree, path, lines):
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = dotted_name(node.func)
            if not name.startswith("subprocess."):
                continue
            for kw in node.keywords:
                if (
                    kw.arg == "shell"
                    and isinstance(kw.value, ast.Constant)
                    and kw.value.value is True
                ):
                    yield self.make(
                        node, path, lines,
                        f"{name} called with shell=True; risk of command injection",
                        name,
                    )
