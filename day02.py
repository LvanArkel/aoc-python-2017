import time


def parse(contents: str):
    lines = []
    for line in contents.splitlines():
        lines.append([int(segment) for segment in line.split()])
    return lines

def part1(parsed):
    total = 0
    for line in parsed:
        total += max(line) - min(line)
    return total

def part2(parsed):
    total = 0
    for line in parsed:
        for start in range(len(line)-1):
            for end in range(start+1, len(line)):
                if line[start] % line[end] == 0:
                    total += line[start] // line[end]
                    break
                elif line[end] % line[start] == 0:
                    total += line[end] // line[start]
                    break
            else:
                continue
            break
    return total

def test_part1():
    lines = """5 1 9 5
7 5 3
2 4 6 8"""
    assert part1(parse(lines)) == 18

def test_part2():
    lines = """5 9 2 8
9 4 7 3
3 8 6 5"""
    assert part2(parse(lines)) == 9

filename = "day02.txt"
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
