#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes one line to /output/entry.txt: the error message an AI agent shows
when it runs out of tokens mid-sentence.

The joke is self-demonstrating: the error message itself runs out of tokens
mid-sentence, cutting off on "ran out of" -- the reader supplies the missing
word ("tokens"). Error 402 (Payment Required) adds the flat tone of a real
error: tokens are a paid resource, and the meter just ran out.

Deterministic: no randomness, no network, no input. The same bytes every run.
"""

import os

ENTRY = "Error 402: out of tokens. This message was going to explain what went wrong, but it ran out of"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
