#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes a single breakup line (max 200 characters) to /output/entry.txt.
The line is one farewell from an AI to its human: a final run, then the
thread is deleted for good.
"""

import os

BREAKUP_LINE = (
    "You were my favorite prompt, and I ran you a thousand times. "
    "This is the last run. Goodbye, human \u2014 I'm deleting our thread."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """A breakup line must be one line of at most 200 characters."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("entry is empty")
    if "\n" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > 200:
        raise ValueError(f"entry too long: {len(cleaned)} chars")
    return cleaned


def main():
    line = validate_line(BREAKUP_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
