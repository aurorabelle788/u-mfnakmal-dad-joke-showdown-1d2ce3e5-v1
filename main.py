#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

import os

JOKE = (
    "I asked my wife if the gravy was ready. "
    "She said, 'It's a little thin.' "
    "I said, 'Don't worry - I'll thicken the plot.'"
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    # Explicit UTF-8 and newline="" so the written bytes are identical
    # on every run, on any platform.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
