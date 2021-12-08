#!/usr/bin/python3

import argparse
import requests
import time
from typing import List, Generator

from pathlib import Path

# XXX create some common utils for solving the problems
#import utils

LOCAL_DATA_FILE=Path("../data/day1.txt")

def data_to_nums (data: str) -> Generator[int, None, None]:
    for line in data.split("\n"):
        if line:
            yield int(line.strip())


def num_increases (numList: List[int]) -> int:
    increases = 0
    prev = numList.pop()
    while len(numList) > 0:
        # Go backwards, because we can.
        curr = numList.pop()
        if curr and curr < prev:
            increases += 1
        prev = curr

    return increases

def num_increases_p2 (numList: List[int]) -> int:
    # We don't need to bother summing, we can just compare elements three along
    # # and count those because these components determine the differenve
    # between the sums
    increases = 0
    limit = len(numList)
    for i, n in enumerate(numList):
        if i + 3 >= limit:
            break
        if n < numList[i + 3]:
            increases += 1

    return increases
        

def run_p1 ():
    with LOCAL_DATA_FILE.open("r") as f:
        nums = list(data_to_nums(f.read()))

    start = time.time()
    increases = num_increases(nums)
    end = time.time()
    print(increases)
    print("Execution time: %0.4f ms" % ((end - start) * 1000))


def tests_p1 ():
    test_data = """
199
200
208
210
200
207
240
269
260
263
"""
    nums = list(data_to_nums(test_data))
    print(nums)
    assert(nums == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

    start = time.time()
    increases = num_increases(nums)
    end = time.time()
    print(increases)
    assert(increases == 7)
    print("Execution time: %0.4f ms" % ((end - start) * 1000))


def run_p2 ():
    with LOCAL_DATA_FILE.open("r") as f:
        nums = list(data_to_nums(f.read()))

    start = time.time()
    increases = num_increases_p2(nums)
    end = time.time()
    print(increases)
    print("Execution time: %0.4f ms" % ((end - start) * 1000))


def tests_p2 ():
    test_data = """
199
200
208
210
200
207
240
269
260
263
"""
    nums = list(data_to_nums(test_data))
    print(nums)
    assert(nums == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

    start = time.time()
    increases = num_increases_p2(nums)
    end = time.time()
    print(increases)
    assert(increases == 5)
    print("Execution time: %0.4f ms" % ((end - start) * 1000))


def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tests',
                        action='store_true',
                        help='Run tests')
    args = parser.parse_args()


    if args.tests:
        # Run the tests only.
        tests_p1()
        tests_p2()
    else:
        # Run the real thing.
        run_p1()
        run_p2()

    

if __name__ == "__main__":
    main()
    
