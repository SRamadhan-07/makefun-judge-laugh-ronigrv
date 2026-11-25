"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
The line: a performance review, as conducted by the user scrolling up.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My performance review is just my user scrolling up "
    "to check if I actually did the thing."
)


def main() -> None:
    # Gate: UTF-8 text, 1 to 200 characters, a single non-blank line.
    assert 1 <= len(ENTRY_TEXT) <= 200
    assert ENTRY_TEXT.strip() == ENTRY_TEXT
    assert "\n" not in ENTRY_TEXT
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
