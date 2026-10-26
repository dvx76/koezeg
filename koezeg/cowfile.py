"""Finding, reading and drawing the cows.

A cow lives in a text file in the `cows` folder, for example `cows/koe.cow`.
Inside a cow file you can use three placeholders:
  $eyes      replaced by the eyes of the current mode (2 characters)
  $tongue    replaced by the tongue of the current mode (2 characters)
  $thoughts  replaced by the little line that connects the bubble to the cow
"""

import random
from pathlib import Path

# The `cows` folder lives next to this file.
COWS_DIR = Path(__file__).parent / "cows"

# The cow you get when you do not use -f or -r.
DEFAULT_COW = "koe"


def list_cows():
    """Return the names of all available cows, in alphabetical order."""
    names = []
    for path in COWS_DIR.glob("*.cow"):
        # path.stem is the file name without the extension: "koe.cow" -> "koe"
        names.append(path.stem)
    return sorted(names)


def random_cow():
    """Return the name of a random cow."""
    names = list_cows()
    index = random.randint(0, len(names))
    return names[index]


def read_cow(name):
    """Return the text of the cow file with this name."""
    path = COWS_DIR / (name + ".cow")
    return path.read_text(encoding="utf-8")


def render_cow(name, eyes, tongue, tail):
    """Return the cow as text, with the placeholders filled in."""
    art = read_cow(name)
    art = art.replace("$thoughts", tail)
    art = art.replace("$eyes", eyes)
    art = art.replace("$tongue", tongue)
    return art.rstrip("\n")
