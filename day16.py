import time
from unittest import case

from tqdm import tqdm


def parse(contents: str):
    return contents.split(",")

def part1(parsed, size=16):
    circle = [chr(ord("a") + i) for i in range(size)]
    for instruction in parsed:
        match instruction[0]:
            case "s":
                amount = int(instruction[1:]) % size
                circle = circle[-amount:] + circle[:-amount]
            case "x":
                a, b = instruction[1:].split("/")
                a = int(a)
                b = int(b)
                tmp = circle[a]
                circle[a] = circle[b]
                circle[b] = tmp
            case "p":
                a, b = instruction[1:].split("/")
                loc_a = circle.index(a)
                loc_b = circle.index(b)
                circle[loc_a] = b
                circle[loc_b] = a
    return "".join(circle)

def part2(parsed, size=16):
    circle = [chr(ord("a") + i) for i in range(size)]
    visited = {}
    for i in tqdm(range(1_000_000_000)):
        for instruction in parsed:
            match instruction[0]:
                case "s":
                    amount = int(instruction[1:]) % size
                    circle = circle[-amount:] + circle[:-amount]
                case "x":
                    a, b = instruction[1:].split("/")
                    a = int(a)
                    b = int(b)
                    tmp = circle[a]
                    circle[a] = circle[b]
                    circle[b] = tmp
                case "p":
                    a, b = instruction[1:].split("/")
                    loc_a = circle.index(a)
                    loc_b = circle.index(b)
                    circle[loc_a] = b
                    circle[loc_b] = a
        circle_repr = "".join(circle)
        if circle_repr in visited:
            old_i = visited[circle_repr]
            cycle_size = i - old_i
            if (1_000_000_000 - i - 1) % cycle_size == 0:
                print(f"Found i={i}")
                return circle_repr
        visited[circle_repr] = i
    return "".join(circle_repr)

test_input = """s1,x3/4,pe/b"""
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed, size=5) == "baedc"

def test_part2():
    pass

filename = "day16.txt"
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
