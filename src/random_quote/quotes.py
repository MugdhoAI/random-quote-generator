"""Quote data and random selection helpers."""

from dataclasses import dataclass
from datetime import date
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
    Quote("Focus is a superpower in a world full of noise.", "Random Quote Generator"),
    Quote("Done is better than perfect when you are still learning.", "Random Quote Generator"),
    Quote("Your future self is built by what you repeat today.", "Random Quote Generator"),
    Quote("Curiosity turns ordinary days into experiments.", "Random Quote Generator"),
    Quote("Ship small, learn fast, and improve steadily.", "Random Quote Generator"),
    Quote("Attention is the rarest resource you own, so spend it deliberately.", "Random Quote Generator"),
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


def get_daily_quote(day: date | None = None) -> Quote:
    """Return the quote of the day for a date.

    The selection is deterministic: the same date always returns the same
    quote, and the choice cycles through the whole collection.
    """
    chosen_day = day if day is not None else date.today()
    return QUOTES[chosen_day.toordinal() % len(QUOTES)]
