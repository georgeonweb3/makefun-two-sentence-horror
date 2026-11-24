#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes exactly one horror story of exactly two sentences to
/output/entry.txt. Deterministic, standard library only, no network.

The story: a boy's imaginary friend stops visiting him — and the
celebration turns out to be premature. The second sentence re-reads
the first: the friend did not leave, it outgrew the child, and the
thing in the corner of the parents' bedroom now only talks to adults.
The horror is implied, never explained.
"""

from pathlib import Path

STORY = (
    "My son's imaginary friend stopped visiting the day he turned seven, "
    "and we celebrated. "
    "He is nine now, and last night he asked me why the man in the corner "
    "of my bedroom only talks to adults."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = STORY.strip()
    if not text or len(text) > 400:
        raise ValueError("story must be 1-400 characters")
    # Exactly two sentences: two terminal stops, no other sentence ends.
    terminators = sum(1 for ch in text if ch in ".!?")
    if terminators != 2 or not text.endswith((".", "!", "?")):
        raise ValueError("story must be exactly two sentences")
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
