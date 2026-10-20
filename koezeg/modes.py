"""The cow modes: the different faces a cow can make.

Every mode has:
  - flag:   the letter used on the command line (for example "d" for -d)
  - eyes:   exactly 2 characters
  - tongue: exactly 2 characters (two spaces means: no tongue)
  - help:   the text shown by `koezeg -h`
"""

# The face of a normal cow, when no mode flag is given.
DEFAULT_MODE = {"eyes": "oo", "tongue": "  "}

MODES = {
    "borg": {
        "flag": "b",
        "eyes": "==",
        "tongue": "  ",
        "help": "Borg mode",
    },
    "dead": {
        "flag": "d",
        "eyes": "xx",
        "tongue": "U ",
        "help": "Dead mode",
    },
    "greedy": {
        "flag": "g",
        "eyes": "$$",
        "tongue": "  ",
        "help": "Greedy mode (dollar signs in the eyes)",
    },
    "stoned": {
        "flag": "s",
        "eyes": "**",
        "tongue": "U ",
        "help": "Stoned mode",
    },
    "tired": {
        "flag": "t",
        "eyes": "-",
        "tongue": "  ",
        "help": "Tired mode (sleepy eyes)",
    },
    "wired": {
        "flag": "w",
        "eyes": "OO",
        "tongue": "  ",
        "help": "Wired mode (wide open eyes)",
    },
    "youthful": {
        "flag": "y",
        "eyes": "..",
        "tongue": "  ",
        "help": "Youthfull mode (tiny eyes)",
    },
    "paranoid": {
        "flag": "p",
        "eyes": "@@",
        "tongue": "  ",
        "help": "Paranoid mode",
    }
}
