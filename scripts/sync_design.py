#!/usr/bin/env python3
"""Bundle the canonical design standard with the portable design skill."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "DESIGN.md"
    target = root / "skills/gtfol-design/references/design-standard.md"
    expected = (
        b"<!-- Generated from repository DESIGN.md by scripts/sync_design.py. "
        b"Edit the source, then regenerate. -->\n\n" + source.read_bytes()
    )
    current = target.read_bytes() if target.exists() else None
    if current == expected:
        print("Bundled design standard is current.")
        return 0
    if args.check:
        print("Bundled design standard is missing or stale. Run python3 scripts/sync_design.py.")
        return 1
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(expected)
    print("Updated bundled design standard.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
