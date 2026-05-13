import time
from typing import List

initial_pattern = """.#.
..#
###""".splitlines()

def rotate(input, i):
    if i == 0:
        return input
    else:
        size = len(input)
        output = [[None] * size for _ in range(0, size)]
        for row in range(size):
            for col in range(size):
                output[row][col] = input[col][size-1-row]
        output = ["".join(o) for o in output]
        return rotate(output, i-1)

def flip(input, i):
    if i == 1:
        return input[::-1]
    elif i == 2:
        return [line[::-1] for line in input]
    else:
        return input

def transform_input(input) -> List[str]:
    return ["".join(rotate(flip(input, f), r)) for r in range(4) for f in range(3)]

def iteration(pattern, mappings):
    size = len(pattern)
    output = []
    if size % 2 == 0:
        step = 2
    elif size % 3 == 0:
        step = 3
    else:
        return pattern
    for row_index in range(0, size, step):
        new_row = ["" for _ in range(0, step+1)]
        for column_index in range(0, size, step):
            segment = [
                pattern[row_index+i][column_index:column_index+step] for i in range(step)
            ]
            possible_inputs = transform_input(segment)
            found = False
            for possible_input in possible_inputs:
                if possible_input in mappings:
                    result = mappings[possible_input]
                    for i in range(len(result)):
                        new_row[i] += result[i]
                    found = True
                    break
            if not found:
                raise Exception(f"Could not find input {possible_inputs} in {mappings}")
        output.extend(new_row)
    return output

    #
    # if size % 2 == 0:
    #     for row_index in range(0, size, 2):
    #         new_row = ["", "", ""]
    #         for column_index in range(0, size, 2):
    #             segment = [
    #                 pattern[row_index][column_index:column_index+2],
    #                 pattern[row_index+1][column_index:column_index + 2],
    #             ]
    #             possible_inputs = transformed_input2(segment)
    #             found = False
    #             for possible_input in possible_inputs:
    #                 if possible_input in mappings:
    #                     result = mappings[possible_input]
    #                     new_row[0] += result[0]
    #                     new_row[1] += result[1]
    #                     new_row[2] += result[2]
    #                     found = True
    #                     break
    #             if not found:
    #                 raise Exception(f"Could not find input {possible_inputs} in {mappings}")
    #         output.extend(new_row)
    # elif size % 3 == 0:
    #     for row_index in range(0, size, 3):
    #         new_row = ["", "", "", ""]
    #         for column_index in range(0, size, 3):
    #             segment = [
    #                 pattern[row_index][column_index:column_index + 3],
    #                 pattern[row_index + 1][column_index:column_index + 3],
    #                 pattern[row_index + 2][column_index:column_index + 3],
    #             ]
    #             possible_inputs = transformed_input3(segment)
    #             found = False
    #             for possible_input in possible_inputs:
    #                 if possible_input in mappings:
    #                     result = mappings[possible_input]
    #                     new_row[0]+= result[0]
    #                     new_row[1]+= result[1]
    #                     new_row[2]+= result[2]
    #                     new_row[3]+= result[3]
    #                     found = True
    #                     break
    #             if not found:
    #                 raise Exception(f"Could not find input {possible_inputs} in {mappings}")
    #         output.extend(new_row)
    # else:
    #     output = pattern
    # return output

def parse(contents: str):
    mappings = {}
    for line in contents.splitlines():
        input, output = line.split(" => ")
        mappings[input.replace("/", "")] = output.split("/")
    return mappings

def part1(parsed, iterations):
    pattern = initial_pattern
    for _ in range(iterations):
        pattern = iteration(pattern, parsed)
    return sum([line.count("#") for line in pattern])

test_input = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""
test_parsed = parse(test_input)

def test_part1():
    test_result = part1(test_parsed, 2)
    assert test_result == 12, test_result

def test_part2():
    pass

filename = "day21.txt"
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
    print("Part 1:", part1(parsed, 5))
    part1_end = time.time()
    print(f"Part 1 took {part1_end - part1_start} seconds")

    test_part2()
    print("Passed tests for part 2")
    part2_start = time.time()
    print("Part 2:", part1(parsed, 18))
    part2_end = time.time()
    print(f"Part 2 took {part2_end - part2_start} seconds")
