import time

def find_pairs(initial_values, iterations):
    a, b = initial_values
    total = 0
    for _ in range(iterations):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if (a & 0xffff) == (b & 0xffff):
            total += 1
    return total

def generator(init, mult, criteria):
    value = init
    while True:
        value = value * mult % 2147483647
        if value % criteria == 0:
            yield value

def parse(contents: str):
    return [int(line.split(" ")[-1]) for line in contents.splitlines()]

def part1(parsed):
    return find_pairs(parsed, 40_000_000)

def part2(parsed):
    gen_a = generator(parsed[0], 16807, 4)
    gen_b = generator(parsed[1], 48271, 8)
    generators = zip(gen_a, gen_b)
    total = 0
    for (a, b) in [next(generators) for _ in range(5_000_000)]:
        if (a & 0xffff) == (b & 0xffff):
            total += 1
    return total

test_input = """"""
test_parsed = parse(test_input)

def test_part1():
    assert find_pairs([65, 8921], 5) == 1
    assert find_pairs([65, 8921], 40_000_000) == 588

def test_part2():
    assert part2([65, 8921]) == 309

filename = "day15.txt"
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
