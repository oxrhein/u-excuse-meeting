"""Build the entry line for u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.

Writes a single razor-sharp excuse for skipping a pointless meeting to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
The judge pairs excuses head to head and rewards the sharpest, most
relatable laugh -- so the line skips the stock bad-wifi/cat/dentist angle
and lands one surprising turn: the calendar itself has had enough.
"""

import os

ENTRY = (
    "Can't make the sync -- my calendar just filed a restraining order "
    "against this meeting, and I'm siding with the calendar."
)


def build_line() -> str:
    """Return the single entry line, trimmed to one tight line."""
    line = " ".join(ENTRY.split())
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry line is {len(line)} chars, must be 1-200")
    return line


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(build_line() + "\n")


if __name__ == "__main__":
    main()
