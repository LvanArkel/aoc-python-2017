import time


def parse(contents: str):
    # TODO
    pass

def part1(parsed):
    # TODO
    pass

def part2(parsed):
    # TODO
    pass

test_input = """"""
test_parsed = parse(test_input)

def test_part1():
    pass

def test_part2():
    pass

filename = "day0.txt"
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
