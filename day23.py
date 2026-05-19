import time
from unittest import case

def eval(var, registers):
    if isinstance(var, int):
        return var
    return registers[var]


def parse(contents: str):
    instructions = []
    for line in contents.splitlines():
        splitted = line.split()
        opcode = splitted[0]
        arguments = []
        for arg in splitted[1:]:
            try:
                arguments.append(int(arg))
            except:
                arguments.append(arg)
        instructions.append((opcode, arguments))
    return instructions

def part1(instructions):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    program_counter = 0
    mul_count = 0
    while 0 <= program_counter < len(instructions):
        opcode, arguments = instructions[program_counter]
        match opcode:
            case "set":
                registers[arguments[0]] = eval(arguments[1], registers)
                program_counter += 1
            case "sub":
                registers[arguments[0]] -= eval(arguments[1], registers)
                program_counter += 1
            case "mul":
                registers[arguments[0]] *= eval(arguments[1], registers)
                program_counter += 1
                mul_count += 1
            case "jnz":
                condition = eval(arguments[0], registers)
                if condition != 0:
                    program_counter += eval(arguments[1], registers)
                else:
                    program_counter += 1
            case _:
                raise ValueError(f"Opcode {opcode} doesn't exist")
    return mul_count

def part2(instructions):
    registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    program_counter = 0
    breakpoint = 20
    while 0 <= program_counter < len(instructions):
        if program_counter == breakpoint:
            print(registers)
            return None
        opcode, arguments = instructions[program_counter]
        match opcode:
            case "set":
                registers[arguments[0]] = eval(arguments[1], registers)
                program_counter += 1
            case "sub":
                registers[arguments[0]] -= eval(arguments[1], registers)
                program_counter += 1
            case "mul":
                registers[arguments[0]] *= eval(arguments[1], registers)
                program_counter += 1
            case "jnz":
                condition = eval(arguments[0], registers)
                if condition != 0:
                    program_counter += eval(arguments[1], registers)
                else:
                    program_counter += 1
            case _:
                raise ValueError(f"Opcode {opcode} doesn't exist")
    return registers['h']

test_input = """"""
test_parsed = parse(test_input)

def test_part1():
    pass

def test_part2():
    pass

filename = "day23.txt"
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
