#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single original sentence to /output/entry.txt: an alien
tourist's one-star review of Earth that still compliments the food.
"""

import os
import re

# Fresh angle: alien bureaucracy (a visa for antennae, queuing for
# sunlight, small-talking a toaster) turned by one real dish, nasi goreng.
SENTENCE = (
    "One star: Earth made my antennae fill out a visa, queue for sunlight, "
    "and small-talk a toaster, but the nasi goreng was so good I forgave "
    "the whole planet mid-bite."
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    terminators = re.findall(r"[.!?]", text)
    if len(terminators) != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
