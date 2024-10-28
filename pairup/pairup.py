import random
from itertools import islice
from typing import Iterator, Optional, Sequence, TypeVar

T = TypeVar("T")


def shuffled(seq: Sequence[T], rng: Optional[random.Random] = None) -> list[T]:
    """Functionally shuffle a sequence.

    Doesn't mutate the original sequence.

    Example:
    >>> seq = ["A", "B", "C", "D"]
    >>> shuffled(seq, rng=random.Random(42))
    ['A', 'D', 'B', 'C']
    >>> seq
    ['A', 'B', 'C', 'D']
    """
    rng = rng or random.Random()
    return rng.sample(seq, k=len(seq))


def pairs(seq: Sequence[T]) -> Iterator[tuple[T, ...]]:
    """Yield pairs from a sequence.

    Example:
    >>> tuple(pairs("ABCDEFG"))
    (('A', 'B'), ('C', 'D'), ('E', 'F'), ('G',))
    """
    gen = iter(seq)
    while True:
        batch = tuple(islice(gen, 2))
        if len(batch):
            yield batch
        else:
            break


def pairup(
    seq: Sequence[T], rng: Optional[random.Random] = None
) -> Iterator[tuple[T, ...]]:
    rng = rng or random.Random()
    yield from pairs(shuffled(seq))
