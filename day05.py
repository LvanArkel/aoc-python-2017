import time


def parse(contents: str):
    return list(map(int, contents.splitlines()))

def part1(parsed):
    jumps = parsed.copy()
    i = 0
    steps = 0
    while 0 <= i < len(jumps):
        dest = jumps[i]
        jumps[i] += 1
        i += dest
        steps += 1
    return steps

def part2(parsed):
    jumps = parsed.copy()
    i = 0
    steps = 0
    while 0 <= i < len(jumps):
        dest = jumps[i]
        jumps[i] += 1 if dest < 3 else -1
        i += dest
        steps += 1
    return steps

def test_part1():
    assert part1([0, 3, 0, 1, -3]) == 5

def test_part2():
    assert part2([0, 3, 0, 1, -3]) == 10

filename = "day05.txt"
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
