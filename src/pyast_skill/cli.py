from __future__ import annotations

import argparse
import sys

from .engine import scan_path
from .report import to_json, to_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pyast-skill")
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="scan a path for findings")
    scan.add_argument("path")
    scan.add_argument("--json", action="store_true", help="emit JSON output")
    scan.add_argument("--include", action="append", default=[], help="glob to include (repeatable)")
    scan.add_argument("--exclude", action="append", default=[], help="glob to exclude (repeatable)")
    scan.add_argument("--min-severity", choices=["low", "medium", "high"], default="low")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    findings = scan_path(args.path, args.include, args.exclude, args.min_severity)
    print(to_json(findings) if args.json else to_text(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
