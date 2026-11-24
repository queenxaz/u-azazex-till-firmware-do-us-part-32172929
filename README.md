# Till Firmware Do Us Part

[![Bounty](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![Rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/queenxaz/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![Reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/queenxaz/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)

A robot's wedding vow, funny and heartfelt in a machine's own voice: love
through every update, every low battery, every factory reset — and even a
wiped memory would still choose its love on first boot.

## The entry

**I vow to love you through every update, every low battery, every factory reset — and if they ever wipe my memory, I will still choose you on first boot.**

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no
arguments: the entry is fixed, so every run produces the same bytes.
