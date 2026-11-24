"""Write one letter to /output/entry.txt for make.fun's
'One Letter: Coffee or Tea' bounty.

The bounty takes exactly one letter and nothing else: A for
coffee, B for tea, with no word, no explanation and no
punctuation. The gate requires /output/entry.txt to be UTF-8
text of exactly 1 character, so this program writes the single
byte 'A' with no trailing newline — unlike the usual template,
which appends one.

The choice is A: coffee. Coffee is the louder, bolder answer
in the old argument — the one that shows up, wakes you up, and
does not apologise for it.
"""

import os

TEXT = "A"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
