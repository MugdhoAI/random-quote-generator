from datetime import date
import random
import sys

from random_quote.cli import main
from random_quote.quotes import QUOTES, Quote, format_quote, get_daily_quote, get_random_quote


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


def test_daily_quote_is_deterministic_for_a_date():
    day = date(2026, 11, 7)
    assert get_daily_quote(day) == get_daily_quote(day)
    assert get_daily_quote(day) in QUOTES


def test_cli_count_prints_the_requested_number_of_quotes(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["quote", "--count", "3"])
    assert main() == 0
    output = capsys.readouterr().out
    assert sum(1 for line in output.splitlines() if line.startswith('"')) == 3


def test_cli_seed_makes_output_reproducible(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["quote", "--seed", "5", "--count", "2"])
    assert main() == 0
    first = capsys.readouterr().out
    assert main() == 0
    second = capsys.readouterr().out
    assert first == second
