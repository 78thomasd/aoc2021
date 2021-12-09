#!/usr/bin/python3

import argparse
import requests
import time
from typing import List, Generator

from pathlib import Path

import utils


LOCAL_DATA_FILE=Path("../data/day2.txt")
TEST_DATA_FILE=Path("../data/day2_test.txt")

def pos_track (line, ctx):
    direction, num = line.split()
    n = int(num)
    if direction == "up":
        ctx["depth"] -= n
    elif direction == "down":
        ctx["depth"] += n
    elif direction == "forward":
        ctx["horizontal"] += n
    return direction, n

def run_p1 (datafile):
    ctx = {"horizontal" : 0, "depth" : 0}
    l = list(utils.read_input(datafile, pos_track, ctx))
    print(ctx)
    print(ctx["horizontal"] * ctx["depth"])

def aim_track (line, ctx):
    direction, num = line.split()
    n = int(num)
    if direction == "up":
        ctx["aim"] -= n
    elif direction == "down":
        ctx["aim"] += n
    elif direction == "forward":
        ctx["horizontal"] += n
        ctx["depth"]+= n * ctx["aim"]

    return direction, n

def run_p2 (datafile):
    ctx = {"horizontal" : 0, "depth" : 0, "aim" : 0}
    l = list(utils.read_input(datafile, aim_track, ctx))
    print(ctx)
    print(ctx["horizontal"] * ctx["depth"])



def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tests',
                        action='store_true',
                        help='Run tests')
    args = parser.parse_args()


    if args.tests:
        run_p1(TEST_DATA_FILE)
        run_p2(TEST_DATA_FILE)
    else:
        run_p1(LOCAL_DATA_FILE)
        run_p2(LOCAL_DATA_FILE)

    

if __name__ == "__main__":
    main()
    
