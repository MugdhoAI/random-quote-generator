"""Command-line interface for the random quote generator."""

import argparse
import random

from . import __version__
from .quotes import QUOTES, format_quote, get_daily_quote, get_random_quotes


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="quote",
        description="Display a random inspirational quote.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List every quote in the collection.",
    )
    parser.add_argument(
        "--daily",
        action="store_true",
        help="Print the quote of the day instead of a random quote.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed for reproducible random selection.",
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
    if args.list:
        for index, quote in enumerate(QUOTES, start=1):
            print(f'{index}. "{quote.text}" \u2014 {quote.author}')
        return 0
    if args.daily:
        print(format_quote(get_daily_quote()))
        return 0
    rng = random.Random(args.seed) if args.seed is not None else None
    for quote in get_random_quotes(args.count, rng):
        print(format_quote(quote))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
