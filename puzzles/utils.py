#!/usr/bin/python3

from pathlib import Path
from typing import Callable

def read_input (filename: Path, func, ctx):
    with filename.open("r") as f:
        for line in f.readlines():
            yield func(line.strip(), ctx)
