import time


def parse(contents: str):
    grid = {}
    for y, row in enumerate(contents.splitlines()):
        for x, char in enumerate(row):
            if char != ' ':
                grid[(x, y)] = char
    return grid

def part1(grid):
    position = next(val for val in grid.keys() if val[1] == 0)
    collected = []
    direction = (0, 1)
    while True:
        next_pos = (position[0] + direction[0], position[1] + direction[1])
        if next_pos not in grid:
            return "".join(collected)
        next_char: str = grid[next_pos]
        if next_char.isalpha():
            collected.append(next_char)
        elif next_char == '+':
            new_direction = [(direction[1], direction[0]), (-direction[1], -direction[0])]
            for dir in new_direction:
                if (next_pos[0] + dir[0], next_pos[1] + dir[1]) in grid:
                    direction = dir
                    break
        position = next_pos


def part2(grid):
    position = next(val for val in grid.keys() if val[1] == 0)
    count = 0
    direction = (0, 1)
    while True:
        count += 1
        next_pos = (position[0] + direction[0], position[1] + direction[1])
        if next_pos not in grid:
            return count
        next_char: str = grid[next_pos]
        if next_char == '+':
            new_direction = [(direction[1], direction[0]), (-direction[1], -direction[0])]
            for dir in new_direction:
                if (next_pos[0] + dir[0], next_pos[1] + dir[1]) in grid:
                    direction = dir
                    break
        position = next_pos

test_input = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """
test_parsed = parse(test_input)

def test_part1():
    assert part1(test_parsed) == "ABCDEF"

def test_part2():
    result = part2(test_parsed)
    assert result == 38, result

filename = "day19.txt"
if __name__ == '__main__':
    with open(f"inputs/{filename}", "r") as f:
        contents = f.read()
    parse_start = time.time()
    parsed = parse(contents)
    parse_end = time.time()
    print(f"Parsing took {parse_end - parse_start} seconds")

    test_part1()
    print("Passed tests for part 1")
    part1_start = time.time()
    print("Part 1:", part1(parsed))
    part1_end = time.time()
    print(f"Part 1 took {part1_end - part1_start} seconds")

    test_part2()
    print("Passed tests for part 2")
    part2_start = time.time()
    print("Part 2:", part2(parsed))
    part2_end = time.time()
    print(f"Part 2 took {part2_end - part2_start} seconds")
