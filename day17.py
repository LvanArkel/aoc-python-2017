import time
from typing import List, Tuple

from tqdm import tqdm

def spin(
        sequence: List[int],
        position: int,
        n: int,
        skip: int
) -> int:
    new_position = (position + skip) % len(sequence) + 1
    sequence.insert(new_position, n)
    return new_position

def part1(parsed):
    sequence = [0]
    position = 0
    for n in range(2017):
        position = spin(sequence, position, n+1, parsed)
    return sequence[(position + 1) % len(sequence)]


def part2(parsed):
    position = 0
    current_value = 0
    for n in tqdm(range(50_000_000)):
        position = (position + parsed) % (n+1) + 1
        if position == 1:
            current_value = n+1
    return current_value

def test_part1():
    result = part1(3)
    assert result == 638, result

def test_part2():
    pass

filename = "day0.txt"
if __name__ == '__main__':
    parsed = 304

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
