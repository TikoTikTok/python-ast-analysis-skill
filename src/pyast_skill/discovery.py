from __future__ import annotations

import fnmatch
from pathlib import Path
from typing import Iterable, Iterator

SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".tox", "build", "dist"}


def _matches(path: Path, root: Path, patterns: Iterable[str]) -> bool:
    rel = path.relative_to(root).as_posix() if root.is_dir() else path.name
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(path.name, p) for p in patterns)


def discover(
    target: str | Path,
    include: list[str] | None = None,
    exclude: list[str] | None = None,
) -> Iterator[Path]:
    root = Path(target)
    if root.is_file():
        candidates = [root] if root.suffix == ".py" else []
    else:
        candidates = sorted(
            p for p in root.rglob("*.py")
            if not any(part in SKIP_DIRS for part in p.relative_to(root).parts)
        )
    for p in candidates:
        if include and not _matches(p, root, include):
            continue
        if exclude and _matches(p, root, exclude):
            continue
        yield p
