# Pairup

A utility for creating pairs.

## Installation

`pairup` is a pure python package with no external dependencies. Requires `Python>=3.10`.

Via pip:

```bash
pip install 'pairup @ git+https://git@github.com/ogaday/pairup'
```

Via poetry:

```bash
poetry add git+https://git@github.com/ogaday/pairup
```

## Usage

`pairup` is a library and CLI.

CLI usage:

```bash
pairup --help
# usage: pairup [-h] [--infile INFILE] [--outfile OUTFILE] [--seed SEED] [--sep SEP] [name ...]

# Randomly pair up a list of names. Accepts multiple name arguments, or a path to a text file containing a list of names. Outputs to stdout, or an output file if supplied. Reproducibility can be be controlled by supplying a random seed.

# positional arguments:
#   name               one or more names to pair up.

# options:
#   -h, --help         show this help message and exit
#   --infile INFILE    an input file to take names from. Must have one name per line.
#   --outfile OUTFILE  an output file to write pairs to.
#   --seed SEED        a random seed, eg. 42.
#   --sep SEP          pairs members are separated by this string. Default ','
```

The library provides three functions: `pairs`, `shuffled`, and `pairup`

```python
>>> import random
>>> from pairup import pairs, shuffled, pairup
>>> names = ['Alice', 'Bob', 'Charlie', 'David']
>>> list(shuffled(names, rng=random.Random(42)))
['Alice', 'David', 'Bob', 'Charlie']
>>> list(pairs(names))
[('Alice', 'Bob'), ('Charlie', 'David')]
>>> list(pairup(names, rng=random.Random(42)))
[('Alice', 'David'), ('Bob', 'Charlie')]

```
