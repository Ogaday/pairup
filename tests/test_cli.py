"""CLI Tests."""
from pathlib import Path

import pytest

from pairup.cli import CLI


def test_pairup_args(cli: CLI, outfile: Path):
    names = ["Alice", "Bob", "Charlie"]
    cli(args=[*names, "--outfile", str(outfile)])

    with open(outfile) as f:
        output = sum([pair.strip().split(",") for pair in f.readlines()], start=[])
    assert names == sorted(output)


def test_pairup_args_seed(cli: CLI, outfile: Path):
    names = ["Alice", "Bob", "Charlie"]
    cli(args=[*names, "--outfile", str(outfile), "--seed", "42"])
    expected = "Charlie,Alice\nBob\n"

    with open(outfile) as f:
        assert f.read() == expected


def test_pairup_infile(cli: CLI, infile: Path, outfile: Path):
    cli(args=["--infile", str(infile), "--outfile", str(outfile), "--seed", "42"])
    expected = "Charlie,Alice\nBob\n"
    with outfile.open("r") as f:
        assert f.read() == expected


def test_pairup_names_and_infile(cli: CLI, infile: Path):
    with pytest.raises(SystemExit):
        cli(args=["--infile", str(infile), "Alice", "Bob", "Charlie"])


def test_pairup_no_names_or_infile(cli: CLI):
    cli(args=[])


def test_pairup_sep(cli: CLI, outfile: Path):
    names = ["Alice", "Bob", "Charlie"]
    cli(args=[*names, "--outfile", str(outfile), "--seed", "42", "--sep", "|"])
    expected = "Charlie|Alice\nBob\n"

    with open(outfile) as f:
        assert f.read() == expected
