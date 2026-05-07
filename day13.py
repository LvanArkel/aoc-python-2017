import time


def parse(contents: str):
    walls = {}
    for line in contents.splitlines():
        splitted = line.split(": ")
        walls[int(splitted[0])] = int(splitted[1])
    return walls

def part1(parsed):
    result = 0
    for pos, length in parsed.items():
        if pos % ((length - 1) * 2) == 0:
            result += pos * length
    return result

def part2(parsed):
    delay = 0
    while True:
        detected = False
        for pos, length in parsed.items():
            if (pos+delay) % ((length - 1) * 2) == 0:
                detected = True
                break
        if not detected:
            return delay
        delay += 1

test_input = """0: 3
1: 2
4: 4
6: 4"""
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed) == 24

def test_part2():
    assert part2(test_parsed) == 10

filename = "day13.txt"
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
