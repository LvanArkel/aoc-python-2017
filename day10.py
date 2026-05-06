import operator
import time
from functools import reduce
from typing import List

def twist(size: int, lengths: List[int], repetitions: int = 1):
    position = 0
    skip_size = 0
    band = list(range(size))
    for _ in range(repetitions):
        for length in lengths:
            swap_count = length // 2
            start = position
            end = (position + length - 1) % size
            for _ in range(swap_count):
                tmp = band[start]
                band[start] = band[end]
                band[end] = tmp
                start = (start + 1) % size
                end = (end - 1) % size
            position = (position + length + skip_size) % size
            skip_size += 1
    return band


def parse(contents: str):
    return contents

def part1(parsed):
    lengths =  [int(segment) for segment in parsed.split(",")]
    band = twist(256, lengths)
    return band[0] * band[1]

def part2(parsed):
    sequence = [ord(c) for c in parsed] + [17, 31, 73, 47, 23]
    band = twist(256, sequence, repetitions=64)
    result = ""
    for i in range(0, len(band), 16):
        numbers = band[i:i + 16]
        dense = reduce(operator.xor, numbers)
        result += f"{dense:02x}"
    return result

def test_part1():
    band = twist(5, [3, 4, 1, 5])
    assert band[0]*band[1] == 12

def test_part2():
    assert part2("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

filename = "day10.txt"
if __name__ == '__main__':
    with open(f"inputs/{filename}", "r") as f:
        contents = f.read()
    parse_start = time.time()
    parsed = parse(contents)
    parse_end = time.time()
    print(f"Parsing took {parse_end - parse_start} seconds")

    test_part1()
    part1_start = time.time()
    print("Part 1:", part1(parsed))
    part1_end = time.time()
    print(f"Part 1 took {part1_end - part1_start} seconds")

    test_part2()
    part2_start = time.time()
    print("Part 2:", part2(parsed))
    part2_end = time.time()
    print(f"Part 2 took {part2_end - part2_start} seconds")
