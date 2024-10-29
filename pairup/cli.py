"""The command line interface."""
import argparse
import random
import sys
from typing import Optional

from pairup import pairup


class CLI:
    """
    A pairup CLI instance.

    Example:
    >>> cli = CLI()
    >>> cli(args=["Alice", "Bob", "Charlie", "--seed", "42"])
    Charlie,Alice
    Bob
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=__package__,
            description=(
                "Randomly pair up a list of names. Accepts multiple name arguments, or "
                "a path to a text file containing a list of names. Outputs to stdout, "
                "or an output file if supplied."
            ),
        )
        self.parser.add_argument(
            "name", nargs="*", help="one or more names to pair up."
        )
        self.parser.add_argument(
            "--infile",
            type=argparse.FileType("r"),
            default=None,
            help="an input file to take names from. Must have one name per line.",
        )
        self.parser.add_argument(
            "--outfile",
            type=argparse.FileType("w"),
            default=sys.stdout,
            help="an output file to write pairs to.",
        )
        self.parser.add_argument("--seed", type=int, help="a random seed, eg. 42.")
        self.parser.add_argument(
            "--sep",
            type=str,
            default=",",
            help="pairs members are separated by this string. Default ','",
        )

    def __call__(self, args: Optional[list[str]] = None):
        """Call the CLI.

        Args:
            args: A list of textual arguments to pass to the the CLI. See CLI
                help text for more details. Default `None` (reads arguments from
                `stdin`).
        """
        parsed = self.parser.parse_args(args)
        rng = random.Random(parsed.seed)

        if not (parsed.infile or parsed.name):
            self.help()
            return
        if parsed.infile and parsed.name:
            sys.exit(
                "Error: Player names must be provided as arguments or via a file, but not both."
            )

        if parsed.infile:
            elements = list(map(str.strip, parsed.infile.readlines()))
        else:
            elements = parsed.name
        for pair in pairup(elements, rng=rng):
            print(parsed.sep.join(pair), file=parsed.outfile)

    def help(self):
        """Print the help text."""
        self.parser.print_help()
