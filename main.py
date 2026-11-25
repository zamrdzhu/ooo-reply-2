"""Funniest One-Line Out-of-Office Reply — one funny line.

A real away message with one turn: the owner is out until Monday,
and the inbox has been left in the care of a cat who has already
deleted everything important. It reads like a message a person
would gladly switch on — no beach, no inbox-zero cliche, no
signature needed, and the laugh lands on the first read. The cat
is the fresh turn on the usual away message: the cover is worse
than the absence.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 160-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = "I'm out of office until Monday. My inbox is being watched by my cat, who has already deleted everything important."


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"error: line is {len(LINE)} chars, must be 1-160",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
