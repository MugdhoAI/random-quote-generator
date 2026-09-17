import random

from random_quote.cli import main
from random_quote.quotes import QUOTES, Quote, format_quote, get_random_quote


def test_quote_collection_is_not_empty():
    assert QUOTES


def test_random_quote_returns_a_known_quote():
    quote = get_random_quote(random.Random(7))
    assert quote in QUOTES


def test_seeded_random_generator_is_deterministic():
    first = get_random_quote(random.Random(42))
    second = get_random_quote(random.Random(42))
    assert first == second


def test_format_quote():
    quote = Quote("Keep going.", "Test Author")
    assert format_quote(quote) == '"Keep going."\n— Test Author'


def test_cli_prints_a_quote(capsys):
    assert main() == 0
    output = capsys.readouterr().out
    assert output.startswith('"')
    assert "— Random Quote Generator" in output
