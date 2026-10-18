from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from typing import Iterable

SEVERITY_ORDER = {"low": 0, "medium": 1, "high": 2}


@dataclass
class Finding:
    rule_id: str
    severity: str
    message: str
    file: str
    line: int
    col: int
    symbol: str
    snippet: str
    confidence: str | None = None

    def to_dict(self) -> dict:
        d = asdict(self)
        if d["confidence"] is None:
            del d["confidence"]
        return d


class Rule:
    rule_id = ""
    severity = "low"
    description = ""

    def check(self, tree: ast.AST, path: str, source_lines: list[str]) -> Iterable[Finding]:
        raise NotImplementedError

    def make(
        self,
        node: ast.AST,
        path: str,
        lines: list[str],
        message: str,
        symbol: str,
        severity: str | None = None,
        confidence: str | None = None,
    ) -> Finding:
        line = getattr(node, "lineno", 1)
        snippet = lines[line - 1].strip() if 0 < line <= len(lines) else ""
        return Finding(
            rule_id=self.rule_id,
            severity=severity or self.severity,
            message=message,
            file=path,
            line=line,
            col=getattr(node, "col_offset", 0),
            symbol=symbol,
            snippet=snippet,
            confidence=confidence,
        )


def dotted_name(node: ast.AST) -> str:
    """Return a dotted name for Name/Attribute chains, else ''."""
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return ".".join(reversed(parts))
    return ""
