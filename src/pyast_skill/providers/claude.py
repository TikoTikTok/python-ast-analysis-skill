from .base import Provider


class ClaudeProvider(Provider):
    """Deterministic stub; no API calls."""

    name = "claude"

    def explain(self, finding: dict) -> str:
        return f"[claude-stub] {finding.get('rule_id')}: review {finding.get('file')}:{finding.get('line')}"
