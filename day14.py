import time

from day10 import part2 as day10_part2

def part1(parsed):
    result = 0
    for row in range(128):
        text = f"{parsed}-{row}"
        hash = day10_part2(text)
        b = bytes.fromhex(hash)
        result += sum([byte.bit_count() for byte in b])
    return result

def part2(parsed):
    grid = []
    for row in range(128):
        text = f"{parsed}-{row}"
        hash = day10_part2(text)
        b = bytes.fromhex(hash)
        grid.append("".join(format(byte, '08b') for byte in b))
    coordinates = [(x, y) for x in range(128) for y in range(128) if grid[y][x] == "1"]
    regions = 0
    while len(coordinates) > 0:
        regions += 1
        visited = set()
        frontier = [coordinates.pop(0)]
        while len(frontier) > 0:
            node = frontier.pop(0)
            if node in visited:
                continue
            visited.add(node)
            neighbours = [
                (node[0] + x, node[1] + y)
                for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            ]
            for neighbour in neighbours:
                if neighbour in coordinates:
                    coordinates.remove(neighbour)
                    frontier.append(neighbour)
    return regions

def test_part1():
    test_result = part1("flqrgnkx")
    assert test_result == 8108

def test_part2():
    assert part2("flqrgnkx") == 1242

filename = "day0.txt"
if __name__ == '__main__':
    parsed = "ffayrhll"

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
