#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes one line of awkward robot small talk to /output/entry.txt
(or to the path given as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "So… do you also count the floor numbers out loud to avoid "
    "eye contact, or is that just my firmware?"
)


def main() -> None:
    # The gate only accepts a single line of 1-200 characters: check the
    # line before writing so a bad edit fails loudly here, not at judging.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    out.chmod(0o644)


if __name__ == "__main__":
    main()
