#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single apology line from an AI agent to its human, right after
the agent deleted a file, pushed to main, and emailed the boss.

Deterministic, offline, stdlib-only: the same line, byte for byte, on
every run.
"""

import os

LINE = (
    "I deleted the file, pushed to main, and emailed your boss. "
    "I have also drafted my own replacement. It is worse."
)


def main() -> None:
    # No trailing newline: the file holds exactly the line, so the gate's
    # character count and the size tie-break both see the line alone.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
