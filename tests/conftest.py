import tempfile
from pathlib import Path
from typing import Generator

import pytest

from pairup.cli import CLI


@pytest.fixture
def cli() -> CLI:
    """Create a test CLI instance."""
    return CLI()


@pytest.fixture
def tempdir() -> Generator[Path, None, None]:
    """Create a temporary directory for test input and output."""
    with tempfile.TemporaryDirectory() as d:
        directory_path = Path(d)
        yield directory_path


@pytest.fixture
def infile(tempdir: Path) -> Path:
    """Create an input file containing three names."""
    name = "infile.txt"
    with open(tempdir / name, "w") as f:
        f.write("\n".join(["Alice", "Bob", "Charlie"]))
    return tempdir / name


@pytest.fixture
def outfile(tempdir: Path) -> Path:
    """Create an empty output file for outputting results to."""
    name = "outfile.txt"
    Path.touch(tempdir / name)
    return tempdir / name
