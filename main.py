#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set). It must be UTF-8 text of 1 to 280 Unicode code points, not only
whitespace, per the bounty gate in RULES.txt.
"""

import os
import sys

JOKE = (
    "I asked my AI agent for a one-line fix \u2014 it rewrote 400 lines, "
    "and the only line it didn't touch was the one with the bug."
)


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > 280:
        print(f"joke is {len(text)} code points; must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the joke, nothing extra
    # for the judge to read.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
