import time


def parse(contents: str):
    return contents.splitlines()

def part1_valid(line: str) -> bool:
    splitted = line.split(" ")
    return len(splitted) == len(set(splitted))

def part1(parsed):
    return len(list(filter(part1_valid, parsed)))

def part2_valid(line: str) -> bool:
    splitted = ["".join(sorted(word)) for word in line.split(" ")]
    return len(splitted) == len(set(splitted))

def part2(parsed):
    return len(list(filter(part2_valid, parsed)))

def test_part1():
    assert part1_valid("aa bb cc dd ee")
    assert not part1_valid("aa bb cc dd aa")
    assert part1_valid("aa bb cc dd aaa")

def test_part2():
    assert part2_valid("abcde fghij")
    assert not part2_valid("abcde xyz ecdab")
    assert part2_valid("a ab abc abd abf abj")
    assert part2_valid("iiii oiii ooii oooi oooo")
    assert not part2_valid("oiii ioii iioi iiio")

filename = "day04.txt"
if __name__ == '__main__':
    test_part1()
    test_part2()

    with open(f"inputs/{filename}", "r") as f:
        contents = f.read()
    parse_start = time.time()
    parsed = parse(contents)
    parse_end = time.time()
    print(f"Parsing took {parse_end - parse_start} seconds")

    part1_start = time.time()
    print("Part 1:", part1(parsed))
    part1_end = time.time()
    print(f"Part 1 took {part1_end - part1_start} seconds")

    part2_start = time.time()
    print("Part 2:", part2(parsed))
    part2_end = time.time()
    print(f"Part 2 took {part2_end - part2_start} seconds")
