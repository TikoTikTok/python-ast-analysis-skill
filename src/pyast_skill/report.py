from __future__ import annotations

import json

from .rules import Finding


def to_json(findings: list[Finding]) -> str:
    return json.dumps(
        {"count": len(findings), "findings": [f.to_dict() for f in findings]}, indent=2
    )


def to_text(findings: list[Finding]) -> str:
    if not findings:
        return "No findings."
    lines = [
        f"{f.file}:{f.line}:{f.col}: {f.rule_id} [{f.severity}] {f.message}"
        for f in findings
    ]
    lines.append(f"{len(findings)} finding(s).")
    return "\n".join(lines)
