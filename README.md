# Random Quote Generator

A simple command line app that displays a random inspirational quote.

## Installation

```bash
python -m pip install -e ".[test]"
```

## Usage

Print one random quote:

```bash
quote
```

Example:

```text
"Progress matters more than perfection."
— Random Quote Generator
```

Print several quotes at once:

```bash
quote --count 3
```

Print the quote of the day (the same quote all day, changing daily):

```bash
quote --daily
```

Make random selection reproducible with a seed:

```bash
quote --seed 42 --count 3
```

List every quote in the collection:

```bash
quote --list
```

## Development

```bash
python -m pytest
```

## License

MIT
