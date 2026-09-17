"""Command-line interface for the random quote generator."""

import argparse

from . import __version__
from .quotes import format_quote, get_random_quote


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    return argparse.ArgumentParser(
        prog="quote",
        description="Display a random inspirational quote.",
    )


def main() -> int:
    """Run the command-line application."""
    parser = build_parser()
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    parser.parse_args()
    print(format_quote(get_random_quote()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
