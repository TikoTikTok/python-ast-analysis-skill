from .base import Provider
from .claude import ClaudeProvider
from .hermes import HermesProvider

_PROVIDERS: dict[str, type[Provider]] = {
    "hermes": HermesProvider,
    "claude": ClaudeProvider,
}


def get_provider(name: str) -> Provider:
    try:
        return _PROVIDERS[name.lower()]()
    except KeyError:
        raise ValueError(f"unknown provider: {name!r}; available: {sorted(_PROVIDERS)}") from None


def available() -> list[str]:
    return sorted(_PROVIDERS)
