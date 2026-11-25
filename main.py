#!/usr/bin/env python3
"""Invent a Word We Need — entrypoint.

Coins one new English word and defines it in a single line, then writes
that line to /output/entry.txt. Standard library only.

The word: doorjog — the hurried little run you do when someone holds
the door open too early. It names a moment everyone recognises at once
and English has no word for. Built from two plain English morphemes
(door + jog), so it is sayable, spellable and memorable at first sight,
and the definition lands in one reading with no second sentence.
"""

import os

ENTRY = (
    "doorjog (n.) the hurried little run you do when someone "
    "holds the door open too early."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-140")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single clean line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
