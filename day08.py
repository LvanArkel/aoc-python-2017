import re
import time
from collections import defaultdict


# Tuple [a,b,c,d,e,f]
# A B C if D E F

def parse(contents: str):
    pattern = re.compile(r"(\w+) (dec|inc) (-?\d+) if (\w+) (\S+) (-?\d+)")
    lines = []
    for line in contents.splitlines():
        match = pattern.match(line)
        if not match:
            raise ValueError(f"Invalid format: {line}")
        lines.append((
            match.group(1),
            match.group(2),
            int(match.group(3)),
            match.group(4),
            match.group(5),
            match.group(6),
        ))
    return lines

def part1(parsed):
    memory = defaultdict(int)
    for (dst, chg, diff, src, cond, cmp) in parsed:
        src_val = memory[src]
        condition = eval(f"{src_val} {cond} {cmp}")
        if condition:
            if chg == "inc":
                memory[dst] += diff
            else:
                memory[dst] -= diff
    return max(memory.values())

def part2(parsed):
    max_memory = 0
    memory = defaultdict(int)
    for (dst, chg, diff, src, cond, cmp) in parsed:
        src_val = memory[src]
        condition = eval(f"{src_val} {cond} {cmp}")
        if condition:
            if chg == "inc":
                memory[dst] += diff
            else:
                memory[dst] -= diff
            max_memory = max(max_memory, memory[dst])
    return max_memory

test_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed) == 1

def test_part2():
    assert part2(test_parsed) == 10

filename = "day08.txt"
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
