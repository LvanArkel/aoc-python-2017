import time


def parse(contents: str):
    paths = dict()
    for line in contents.splitlines():
        src, dest = line.split(" <-> ")
        paths[src] = dest.split(", ")
    return paths

def part1(parsed):
    visited = set()
    frontier = ["0"]
    while len(frontier) > 0:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        frontier.extend(parsed[node])
    return len(visited)

def part2(parsed):
    groups = 0
    all_nodes = set(parsed.keys())
    while len(all_nodes) > 0:
        groups += 1
        visited = set()
        frontier = [all_nodes.pop()]
        while len(frontier) > 0:
            node = frontier.pop()
            if node in visited:
                continue
            visited.add(node)
            frontier.extend(parsed[node])
        all_nodes = all_nodes.difference(visited)
    return groups

test_input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed) == 6

def test_part2():
    assert part2(test_parsed) == 2

filename = "day12.txt"
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
