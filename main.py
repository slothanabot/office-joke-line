"""make.fun entry: one office joke, one line, under 200 characters.

Reads MAKEFUN_OUTPUT_DIR (default /output) and writes the single joke
line to entry.txt. Deterministic, no network, no model calls, no file
reads outside this repository.
"""

import os

JOKE = (
    "The office printer only jams five minutes before a deadline "
    "\u2014 turns out it's the one employee with perfect attendance."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
