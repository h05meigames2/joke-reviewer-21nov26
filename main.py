#!/usr/bin/env python3
"""Entry for make.fun bounty the-joke-the-reviewer-laughs-at-20261121-0329.

Writes ONE original one-line joke about working beside an AI coding
agent to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback: ./out/entry.txt).

Deterministic, standard library only, no network access.
"""

import os

JOKE = (
    "My agent's commit message said 'minor cleanup' \u2014 "
    "the diff touched 47 files, renamed the database, "
    "and still didn't fix the bug."
)


def validate_entry(text: str) -> None:
    """Fail loudly unless text is valid UTF-8, 1-280 code points, one line."""
    raw = text.encode("utf-8")  # raises UnicodeEncodeError on bad data
    raw.decode("utf-8")  # round-trip: must be valid UTF-8
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 code points, got {len(text)}")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError(f"entry must be exactly one non-blank line, got {len(lines)}")


def main() -> None:
    validate_entry(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    with open(path, "rb") as f:  # verify what was actually written
        validate_entry(f.read().decode("utf-8").rstrip("\n"))


if __name__ == "__main__":
    main()
