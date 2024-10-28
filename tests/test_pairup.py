import random
from typing import Sequence

import pytest

from pairup.pairup import T, pairs, shuffled


def test_shuffled():
    # Arrange
    seq = ["A", "B", "C", "D"]

    # Act
    new = shuffled(seq)

    # Assert
    assert sorted(new) == seq
    assert seq == ["A", "B", "C", "D"]


def test_shuffled_seed():
    # Arrange
    rng = random.Random(42)
    seq = ["A", "B", "C", "D"]

    # Act
    new = shuffled(seq, rng=rng)

    # Assert
    assert sorted(new) == seq
    assert new == ["A", "D", "B", "C"]


@pytest.mark.parametrize(
    "input, output",
    [
        ("ABCD", (("A", "B"), ("C", "D"))),
        ("ABCDE", (("A", "B"), ("C", "D"), ("E",))),
        ((), ()),
    ],
)
def test_pairs(input: Sequence[T], output: tuple[tuple[T, ...], ...]):
    assert tuple(pairs(input)) == output
