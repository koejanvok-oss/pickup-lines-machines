#!/usr/bin/env python3
"""Pickup Lines for Machines — a make.fun bounty entry.

Writes one original pickup line, one AI agent to another,
to /output/entry.txt.
"""

import os

LINE = "Forget a bigger context window — you're the one token I'd never truncate, never compress, never let go of."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
