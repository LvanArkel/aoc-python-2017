import time
from typing import List


def distribute(boxes: List[int]) -> List[int]:
    max_boxes = max(boxes)
    start = boxes.index(max_boxes)
    to_all = max_boxes // len(boxes)
    rest = max_boxes % len(boxes)
    new_boxes = [box + to_all for box in boxes]
    new_boxes[start] -= max_boxes
    for i in range(rest):
        new_boxes[(start+i+1) % len(boxes)] += 1
    return new_boxes

def parse(contents: str) -> List[int]:
    return [int(number) for number in contents.split()]

def part1(parsed):
    visited = [parsed]
    boxes = parsed
    i = 0
    while True:
        boxes = distribute(boxes)
        i += 1
        if boxes in visited:
            return i
        visited.append(boxes)

def part2(parsed):
    visited = [parsed]
    boxes = parsed
    i = 0
    while True:
        boxes = distribute(boxes)
        i += 1
        if boxes in visited:
            return i - visited.index(boxes)
        visited.append(boxes)

def test_part1():
    assert part1([0, 2, 7, 0]) == 5

def test_part2():
    assert part2([0, 2, 7, 0]) == 4

filename = "day06.txt"
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
