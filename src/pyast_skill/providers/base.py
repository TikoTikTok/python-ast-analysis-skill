from __future__ import annotations

from abc import ABC, abstractmethod


class Provider(ABC):
    name = ""

    @abstractmethod
    def explain(self, finding: dict) -> str:
        """Return an explanation/remediation for a finding dict."""
