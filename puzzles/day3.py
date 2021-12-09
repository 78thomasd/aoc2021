#!/usr/bin/python3

import argparse
import requests
import time
from typing import List, Generator

from pathlib import Path

import utils


LOCAL_DATA_FILE=Path("../data/day3.txt")
TEST_DATA_FILE=Path("../data/day3_test.txt")

def read_binary (line, ctx):
    if "num_bits" not in ctx:
        ctx["num_bits"] = len(line)
        ctx["bit_counts"] = [0] * ctx["num_bits"]
    
    for i, bit in enumerate(line):
        if bit == "1":
            ctx["bit_counts"][i] += 1
        else:
            assert bit == "0"

    ctx["count"] += 1

    return int(line, 2)

def run_p1 (datafile):
    ctx = {"count": 0}
    l = list(utils.read_input(datafile, read_binary, ctx))
    print(ctx)
    gamma = int(
        "".join("0" if bit < ctx["count"] // 2 else "1"
                for bit in ctx["bit_counts"]),
        2
    )
    epsilon = int(
        "".join("1" if bit < ctx["count"] // 2 else "0"
                for bit in ctx["bit_counts"]),
        2
    )


    print(gamma, epsilon, gamma * epsilon)


def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tests',
                        action='store_true',
                        help='Run tests')
    args = parser.parse_args()


    if args.tests:
        run_p1(TEST_DATA_FILE)
    else:
        run_p1(LOCAL_DATA_FILE)

if __name__ == "__main__":
    main()
    
