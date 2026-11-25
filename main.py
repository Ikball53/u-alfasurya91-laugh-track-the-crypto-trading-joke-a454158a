"""Laugh Track: one crypto trading joke, one line, no filler.

The observation: traders never actually quit a losing coin — they just
rename the loss. The bag stays in the wallet, untouched for months, while
the owner calls it a "long-term hold" to avoid admitting the trade failed.
The twist lands in the last two words: the "promotion" was never earned,
it was just a losing trade rebranded.
"""

from pathlib import Path


def build_joke() -> str:
    """Return the single-line joke (one concrete trading-life observation)."""
    setup = "I didn't lose money on that coin,"
    twist = "I just promoted it to a long-term hold."
    return f"{setup} {twist}"


def main() -> None:
    line = build_joke()
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
