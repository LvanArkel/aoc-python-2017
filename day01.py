import time


def parse(contents: str):
    ls = [int(d) for d in contents]
    ls.append(ls[0])
    return ls

def part1(parsed):
    last_digit = parsed[0]
    total = 0
    for i in range(1, len(parsed)):
        if parsed[i] == last_digit:
            total += last_digit
        else:
            last_digit = parsed[i]
    return total

def part2(parsed):
    total = 0
    half_list = len(parsed)//2
    for i in range(0, half_list):
        if parsed[i] == parsed[i+half_list]:
            total += parsed[i] * 2
    return total

def test_part1():
    test = part1(parse("1122"))
    assert test == 3, test
    test = part1(parse("1111"))
    assert test == 4, test
    test = part1(parse("1234"))
    assert test == 0, test
    test = part1(parse("91212129"))
    assert test == 9, test

def test_part2():
    test = part2(parse("1212"))
    assert test == 6, test
    test = part2(parse("1221"))
    assert test == 0, test
    test = part2(parse("123425"))
    assert test == 4, test
    test = part2(parse("123123"))
    assert test == 12, test
    test = part2(parse("12131415"))
    assert test == 4, test

filename = "day01.txt"
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
