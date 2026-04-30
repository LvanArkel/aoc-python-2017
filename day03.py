import time
from argparse import ArgumentError
from unittest import case


def ring_start(max):
    if max == 1:
        return 1, 0
    radius = 0
    start = 1
    while True:
        new_start = (2*radius+1)**2 + 1
        if new_start > max:
            return start, radius
        start = new_start
        radius += 1


def part1(parsed):
    start, radius = ring_start(parsed)
    if radius == 0:
        return 0
    ring_diff = parsed - start
    ring_offset = ring_diff % (radius*2)
    return ring_offset + 1

def coordinates(value):
    start, radius = ring_start(value)
    if radius == 0:
        return (0, 0)
    ring_diff = value - start
    ring_segment = ring_diff // (2*radius)
    ring_offset = ring_diff % (2*radius)
    match ring_segment:
        case 0:
            return radius, -(radius - 1) + ring_offset
        case 1:
            return (radius - 1) - ring_offset, radius
        case 2:
            return -radius, radius - 1 - ring_offset
        case 3:
            return -(radius - 1) + ring_offset, -radius
        case _:
            raise Exception(f"Invalid segment {ring_segment} for value {value}")


def part2(parsed):
    value_map = {(0, 0): 1}
    i = 2;
    while True:
        coordinate = coordinates(i)
        neighbours = [(coordinate[0]+x, coordinate[1]+y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]
        value = sum([value_map.get(neighbor, 0) for neighbor in neighbours])
        value_map[coordinate] = value
        if value > parsed:
            return value
        i += 1

def test_part1():
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31

def test_part2():
    assert coordinates(1) == (0, 0)
    assert coordinates(2) == (1, 0)
    assert coordinates(3) == (1, 1)
    assert coordinates(4) == (0, 1)
    assert coordinates(5) == (-1, 1)
    assert coordinates(6) == (-1, 0)
    assert coordinates(7) == (-1, -1)
    assert coordinates(8) == (0, -1)
    assert coordinates(9) == (1, -1)
    assert coordinates(10) == (2, -1)
    assert coordinates(11) == (2, 0)
    assert coordinates(12) == (2, 1)
    assert coordinates(13) == (2, 2)
    assert coordinates(14) == (1, 2)
    assert coordinates(25) == (2, -2)
    assert coordinates(26) == (3, -2)
    assert part2(800) == 806

filename = "day0.txt"
if __name__ == '__main__':

    # with open(f"inputs/{filename}", "r") as f:
    #     contents = f.read()
    # parse_start = time.time()
    # parsed = parse(contents)
    # parse_end = time.time()
    # print(f"Parsing took {parse_end - parse_start} seconds")
    parsed = 277678

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
