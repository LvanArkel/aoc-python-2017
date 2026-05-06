import time

def parse(contents: str):
    return contents

def part1(parsed):
    score = 0
    nexted_level = 0
    in_garbage = False
    skip_next = False
    for c in parsed:
        if skip_next:
            skip_next = False
        elif in_garbage:
            if c == ">":
                in_garbage = False
            elif c == "!":
                skip_next = True
        else:
            if c == "{":
                nexted_level += 1
            elif c == "}":
                score += nexted_level
                nexted_level -= 1
            if c == "<":
                in_garbage = True
    return score

def part2(parsed):
    score = 0
    in_garbage = False
    skip_next = False
    for c in parsed:
        if skip_next:
            skip_next = False
        elif in_garbage:
            if c == ">":
                in_garbage = False
            elif c == "!":
                skip_next = True
            else:
                score += 1
        else:
            if c == "<":
                in_garbage = True
    return score

def test_part1():
    assert part1("{}") == 1
    assert part1("{{{}}}") == 6
    assert part1("{{},{}}") == 5
    assert part1("{{{},{},{{}}}}") == 16
    assert part1("{<a>,<a>,<a>,<a>}") == 1
    assert part1("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert part1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert part1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

def test_part2():
    assert part2("<>") == 0
    assert part2("<random characters>") == 17
    assert part2("<<<<>") == 3
    assert part2("<{!>}>") == 2
    assert part2("<!!>") == 0
    assert part2("<!!!>>") == 0
    assert part2('<{o"i!a,<{i<a>') == 10

filename = "day09.txt"
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
