from __future__ import annotations

import ast
from pathlib import Path

from .discovery import discover
from .rules import Finding, Rule, all_rules
from .rules.base import SEVERITY_ORDER


def scan_source(source: str, path: str = "<string>", rules: list[Rule] | None = None) -> list[Finding]:
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError:
        return []
    lines = source.splitlines()
    findings: list[Finding] = []
    for rule in rules or all_rules():
        findings.extend(rule.check(tree, path, lines))
    return sorted(findings, key=lambda f: (f.file, f.line, f.col, f.rule_id))


def scan_path(
    target: str | Path,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
    min_severity: str = "low",
) -> list[Finding]:
    threshold = SEVERITY_ORDER[min_severity]
    out: list[Finding] = []
    for p in discover(target, include, exclude):
        try:
            source = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        out.extend(f for f in scan_source(source, str(p)) if SEVERITY_ORDER[f.severity] >= threshold)
    return out
