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


def test_cli_daily_prints_one_quote(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["quote", "--daily"])
    assert main() == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 2
    assert lines[0].startswith('"')


def test_random_quotes_have_no_repeats_within_the_collection():
    from random_quote.quotes import get_random_quotes

    for seed in range(20):
        selected = get_random_quotes(len(QUOTES), random.Random(seed))
        assert len(selected) == len(QUOTES)
        assert len(set(selected)) == len(QUOTES)


def test_random_quotes_repeat_only_after_a_full_pass():
    from random_quote.quotes import get_random_quotes

    selected = get_random_quotes(len(QUOTES) + 3, random.Random(3))
    assert len(selected) == len(QUOTES) + 3
    assert len(set(selected[: len(QUOTES)])) == len(QUOTES)


def test_cli_count_prints_distinct_quotes(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["quote", "--seed", "2", "--count", "5"])
    assert main() == 0
    output = capsys.readouterr().out
    printed = [line for line in output.splitlines() if line.startswith('"')]
    assert len(printed) == 5
    assert len(set(printed)) == 5


def test_cli_list_prints_every_quote(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["quote", "--list"])
    assert main() == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == len(QUOTES)
    assert lines[0].startswith("1. ")
