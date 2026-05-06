import time


def parse(contents: str):
    lines = contents.splitlines()
    weights = {}
    tower = {}
    for line in lines:
        splitted = line.split(" -> ")
        title, weight = splitted[0].split(" ")
        weights[title] = int(weight[1:-1])
        if len(splitted) == 2:
            children = splitted[1].split(", ")
            tower[title] = children
    return weights, tower

def node_weight(title, weights, tower, cache):
    if title in cache:
        return cache[title]
    weight = weights[title]
    if title in tower:
        children = tower[title]
        for child in children:
            weight += node_weight(child, weights, tower, cache)
    return weight

def part1(parsed):
    weights, tower = parsed
    all_children = [child for children in tower.values() for child in children]
    return [title for title in tower if title not in all_children][0]

def traverse(tower_root, tower):
    path = []
    frontier = [tower_root]
    while frontier != []:
        current = frontier.pop(0)
        path.append(current)
        frontier.extend(tower.get(current, []))
    return path

def part2(parsed):
    weights, tower = parsed
    cache = {}
    tower_root = part1(parsed)
    path = reversed(traverse(tower_root, tower))
    for node in path:
        if node not in tower:
            continue
        children_weights = [(node_weight(child, weights, tower, cache), child) for child in tower[node]]
        if not all([child[0] == children_weights[0][0] for child in children_weights]):
            sorted_weights = sorted(children_weights)
            if sorted_weights[0][0] == sorted_weights[1][0]:
                diff = sorted_weights[0][0] - sorted_weights[-1][0]
                return weights[sorted_weights[-1][1]] + diff
            else:
                diff = sorted_weights[-1][0] - sorted_weights[0][0]
                return weights[sorted_weights[0][1]] + diff



test_input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed) == "tknk"

def test_part2():
    result = part2(test_parsed)
    assert result == 60, str(result)

filename = "day07.txt"
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
