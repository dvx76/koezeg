"""The command line interface: reads the options and prints the cow."""

import argparse

from koezeg.bubble import make_bubble
from koezeg.cowfile import DEFAULT_COW, random_cow, render_cow
from koezeg.modes import DEFAULT_MODE, MODES

from rich.console import Console

# What the cow says when you give it nothing to say.
DEFAULT_MESSAGE = "Boe!"


def build_parser():
    """Describe which command line options koezeg understands."""
    parser = argparse.ArgumentParser(
        prog="koezeg",
        description="Let a cow say something.",
    )

    parser.add_argument(
        "message",
        nargs="*",
        help="what the cow should say",
    )
    parser.add_argument(
        "-f",
        dest="cow",
        default=DEFAULT_COW,
        metavar="COWFILE",
        help="which cow to use (default: %s)" % DEFAULT_COW,
    )
    parser.add_argument(
        "-r",
        dest="random",
        action="store_true",
        help="use a random cow",
    )

    # One option for every mode in modes.py: -b, -d, -g, ...
    for mode_name, mode in MODES.items():
        parser.add_argument(
            "-" + mode["flag"],
            dest="mode",
            action="store_const",
            const=mode_name,
            help=mode["help"],
        )

    return parser


def main():
    """Run koezeg."""
    args = build_parser().parse_args()

    if len(args.message) > 0:
        message = args.message[0]
    else:
        message = DEFAULT_MESSAGE

    if args.random:
        cow = random_cow()
    else:
        cow = args.cow

    # args.mode is None when no mode flag was given.
    mode = MODES.get(args.mode, DEFAULT_MODE)

    console = Console()
    console.print(make_bubble(message), style="cyan")
    console.print(render_cow(cow, mode["eyes"], mode["tongue"]), style="cyan")
