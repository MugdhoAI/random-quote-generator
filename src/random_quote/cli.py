"""Command-line interface for the random quote generator."""

import argparse

from . import __version__
from .quotes import format_quote, get_random_quote


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="quote",
        description="Display a random inspirational quote.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of quotes to print (default: 1).",
    )
    return parser


def main() -> int:
    """Run the command-line application."""
    parser = build_parser()
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count must be at least 1")
    for _ in range(args.count):
        print(format_quote(get_random_quote()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
