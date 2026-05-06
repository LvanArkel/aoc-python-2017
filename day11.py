import time

def offset(dir: str):
    match dir:
        case "n":
            return (0, -1, 1)
        case "ne":
            return (1, -1, 0)
        case "se":
            return (1, 0, -1)
        case "s":
            return (0, 1, -1)
        case "sw":
            return (-1, 1, 0)
        case "nw":
            return (-1, 0, 1)
        case _:
            raise ValueError(f"Unknown direction {dir}")


def parse(contents: str):
    return contents.split(",")

def part1(parsed):
    coordinate = [0, 0, 0]
    for dir in parsed:
        off = offset(dir)
        coordinate[0] += off[0]
        coordinate[1] += off[1]
        coordinate[2] += off[2]
    return (abs(coordinate[0]) + abs(coordinate[1]) + abs(coordinate[2])) // 2

def part2(parsed):
    max_dist = 0
    coordinate = [0, 0, 0]
    for dir in parsed:
        off = offset(dir)
        coordinate[0] += off[0]
        coordinate[1] += off[1]
        coordinate[2] += off[2]
        max_dist = max(max_dist, (abs(coordinate[0]) + abs(coordinate[1]) + abs(coordinate[2]))//2)
    return max_dist

def test_part1():
    assert part1(parse("ne,ne,ne")) == 3
    assert part1(parse("ne,ne,sw,sw")) == 0
    assert part1(parse("ne,ne,s,s")) == 2
    assert part1(parse("se,sw,se,sw,sw")) == 3

def test_part2():
    pass

filename = "day11.txt"
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
