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


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
