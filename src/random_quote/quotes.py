"""Quote data and random selection helpers."""

from dataclasses import dataclass
import random


@dataclass(frozen=True)
class Quote:
    """A quote and its attribution."""

    text: str
    author: str


QUOTES = (
    Quote("Start where you are. Use what you have. Do what you can.", "Random Quote Generator"),
    Quote("Small steps taken consistently can lead to remarkable progress.", "Random Quote Generator"),
    Quote("A clear goal turns effort into direction.", "Random Quote Generator"),
    Quote("Progress matters more than perfection.", "Random Quote Generator"),
    Quote("The best time to begin is the moment you decide to begin.", "Random Quote Generator"),
    Quote("Keep learning, keep building, and keep moving forward.", "Random Quote Generator"),
    Quote("Difficult work becomes manageable when you take it one step at a time.", "Random Quote Generator"),
    Quote("Consistency gives small actions the power to become big results.", "Random Quote Generator"),
)


def get_random_quote(rng: random.Random | None = None) -> Quote:
    """Return a randomly selected quote.

    An optional random number generator makes selection deterministic in tests
    and allows callers to control randomness when needed.
    """
    generator = rng if rng is not None else random
    return generator.choice(QUOTES)


def format_quote(quote: Quote) -> str:
    """Format a quote for terminal output."""
    return f'"{quote.text}"\n— {quote.author}'
