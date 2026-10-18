from .base import Provider


class HermesProvider(Provider):
    """Deterministic stub; no API calls."""

    name = "hermes"

    def explain(self, finding: dict) -> str:
        return f"[hermes-stub] {finding.get('rule_id')}: review {finding.get('file')}:{finding.get('line')}"
