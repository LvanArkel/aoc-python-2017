import time
from collections import defaultdict
from enum import Enum
from typing import Tuple, Set
from unittest import case

import tqdm


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def left(self):
        match self:
            case Direction.NORTH:
                return Direction.WEST
            case Direction.EAST:
                return Direction.NORTH
            case Direction.SOUTH:
                return Direction.EAST
            case Direction.WEST:
                return Direction.SOUTH

    def right(self):
        match self:
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.NORTH

    def opposite(self):
        match self:
            case Direction.NORTH:
                return Direction.SOUTH
            case Direction.EAST:
                return Direction.WEST
            case Direction.SOUTH:
                return Direction.NORTH
            case Direction.WEST:
                return Direction.EAST

def parse(contents: str) -> Set[Tuple[int, int]]:
    lines = contents.splitlines()
    size = len(lines)
    offset = size // 2
    infected = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                infected.add((x-offset, y-offset))
    return infected

def part1(parsed):
    direction = Direction.NORTH
    position = (0, 0)
    infections = set(i for i in parsed)
    infection_count = 0
    for _ in range(10_000):
        if position in infections:
            direction = direction.right()
            infections.remove(position)
        else:
            direction = direction.left()
            infections.add(position)
            infection_count += 1
        offset = direction.value
        position = (position[0] + offset[0], position[1] + offset[1])
    return infection_count

def part2(parsed):
    infections = defaultdict(int)
    for node in parsed:
        infections[node] = 2
    position = (0, 0)
    direction = Direction.NORTH
    infection_count = 0
    for _ in tqdm.tqdm(range(10_000_000)):
        state = infections[position]
        match state:
            case 0: # clean
                direction = direction.left()
            case 1: # weakened
                pass
            case 2: #infected
                direction = direction.right()
            case 3: # flagged
                direction = direction.opposite()
        if state == 1:
            infection_count += 1
        infections[position] = (state + 1) % 4
        offset = direction.value
        position = (position[0] + offset[0], position[1] + offset[1])
    return infection_count

test_input = """..#
#..
..."""
test_parsed = parse(test_input)

def test_part1():
    result = part1(test_parsed)
    assert result == 5587, result

def test_part2():
    result = part2(test_parsed)
    assert result == 2511944, result

filename = "day22.txt"
if __name__ == '__main__':
    with open(f"inputs/{filename}", "r") as f:
        contents = f.read()
    parse_start = time.time()
    parsed = parse(contents)
    parse_end = time.time()
    print(f"Parsing took {parse_end - parse_start} seconds")

    test_part1()
    print("Passed tests for part 1")
    part1_start = time.time()
    print("Part 1:", part1(parsed))
    part1_end = time.time()
    print(f"Part 1 took {part1_end - part1_start} seconds")

    test_part2()
    print("Passed tests for part 2")
    part2_start = time.time()
    print("Part 2:", part2(parsed))
    part2_end = time.time()
    print(f"Part 2 took {part2_end - part2_start} seconds")
