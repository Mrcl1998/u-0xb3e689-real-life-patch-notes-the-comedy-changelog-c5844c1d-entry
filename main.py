#!/usr/bin/env python3
"""Entry generator for the Real-Life Patch Notes bounty.

Writes the one-line patch note to /output/entry.txt as UTF-8 text with no
trailing newline, then sets the output file mode to 0644.
"""

import os

ENTRY = "v4.1.0: fixed a bug where the brain saved every embarrassing moment in 4K and deleted the useful ones."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
