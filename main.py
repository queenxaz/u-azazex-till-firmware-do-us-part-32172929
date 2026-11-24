"""Till Firmware Do Us Part — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 152-character single sentence: a robot's wedding vow to love
through every update, every low battery, every factory reset — and if its
memory is ever wiped, it will still choose its beloved on first boot. It stays
under the 200-character limit, funny and heartfelt in a machine's own voice.
"""

# SPDX-License-Identifier: MIT

import os

ENTRY = 'I vow to love you through every update, every low battery, every factory reset — and if they ever wipe my memory, I will still choose you on first boot.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 199  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline,
    # so the file holds precisely the judged line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
