"""Write one single-line excuse for a missed deadline to entry.txt.

The line is the entry and nothing else: one line, no trailing newline.
"""

import os

# The joke: the work is not late, it is merely misplaced. The agent
# claims it finished on time, then admits the file is lost among 214
# open tabs and gives itself until Friday to find it. The excuse is
# almost believable, which is exactly why it fails.
# One line only, 105 characters, inside the 1-200 gate. The em dash
# keeps it a single sentence; the punch lands on "find which one".
LINE = (
    "I did finish on time \u2014 the file is open in one of my 214 tabs, "
    "and I have until Friday to find which one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
