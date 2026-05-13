import copy
import re
import time
from typing import List

import tqdm


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError

    def size_manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __copy__(self):
        return Vec3(self.x, self.y, self.z)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

class Point:
    def __init__(self, pos: Vec3, vel: Vec3, acc: Vec3):
        self.position = pos
        self.velocity = vel
        self.acceleration = acc

    def __copy__(self):
        return Point(copy.copy(self.position), copy.copy(self.velocity), copy.copy(self.acceleration))

    def __repr__(self):
        return f"(p={self.position}, v={self.velocity}, a={self.acceleration})"

def parse_match(match: re.Match):
    x = int(match.group(1))
    y = int(match.group(2))
    z = int(match.group(3))
    return Vec3(x, y, z)

def parse(contents: str):
    lines = []
    pattern = re.compile(r"<(\s?-?\d+),(\s?-?\d+),(\s?-?\d+)>")
    for line in contents.splitlines():
        matches = pattern.finditer(line)
        lines.append(
            Point(
                parse_match(next(matches)),
                parse_match(next(matches)),
                parse_match(next(matches)),
            )
        )
    return lines


def part1(parsed: List[Point]):
    points = [copy.copy(point) for point in parsed]
    for _ in tqdm.tqdm(range(10_000)):
        for point in points:
            point.velocity += point.acceleration
            point.position += point.velocity
    min_dist = None
    result = -1
    for i, point in enumerate(points):
        distance = point.position.size_manhattan()
        if min_dist is None or distance < min_dist:
            min_dist = distance
            result = i
    return result


def part2(parsed):
    points = [copy.copy(point) for point in parsed]
    for _ in tqdm.tqdm(range(10_000)):
        duplicates = set()
        visited = set()
        for point in points:
            if point.position in visited:
                duplicates.add(point.position)
            visited.add(point.position)
        points = list(filter(lambda p: p.position not in duplicates, points))
        for point in points:
            point.velocity += point.acceleration
            point.position += point.velocity
    return len(points)

test_input = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""
test_parsed = parse(test_input)

def test_part1():
    result = part1(test_parsed)
    assert result == 0

test2_input = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""
test2_parsed = parse(test2_input)

def test_part2():
    result = part2(test2_parsed)
    assert result == 1

filename = "day20.txt"
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
