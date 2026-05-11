import time
from collections import defaultdict


def try_int(text: str) -> int | str:
    try:
        return int(text)
    except ValueError:
        return text

def parse(contents: str):
    result = []
    for line in contents.splitlines():
        splitted = line.split()
        match splitted[0]:
            case "snd":
                result.append((splitted[0], try_int(splitted[1])))
            case "set":
                result.append((splitted[0], splitted[1], try_int(splitted[2])))
            case "add":
                result.append((splitted[0], splitted[1], try_int(splitted[2])))
            case "mul":
                result.append((splitted[0], splitted[1], try_int(splitted[2])))
            case "mod":
                result.append((splitted[0], splitted[1], try_int(splitted[2])))
            case "rcv":
                result.append((splitted[0], try_int(splitted[1])))
            case "jgz":
                result.append((splitted[0], splitted[1], try_int(splitted[2])))
            case _:
                print("Unknown opcode", splitted)
    return result

def part1(parsed):
    state = defaultdict(int)
    last_played = 0
    program_counter = 0
    def eval(value: int | str) -> int:
        if isinstance(value, int):
            return value
        else:
            return state[value]
    while 0 <= program_counter < len(parsed):
        instruction = parsed[program_counter]
        match instruction[0]:
            case "snd":
                last_played = eval(instruction[1])
            case "set":
                state[instruction[1]] = eval(instruction[2])
            case "add":
                state[instruction[1]] += eval(instruction[2])
            case "mul":
                state[instruction[1]] *= eval(instruction[2])
            case "mod":
                state[instruction[1]] %= eval(instruction[2])
            case "rcv":
                if eval(state[instruction[1]]) != 0:
                    return last_played
            case "jgz":
                if eval(state[instruction[1]]) > 0:
                    program_counter += eval(instruction[2])
                    continue
        program_counter += 1

class Machine:
    def __init__(self, program, machine_id):
        self.program = program
        self.state = defaultdict(int)
        self.state['p'] = machine_id
        self.program_counter = 0
        self.send_buffer = []
        self.receive_buffer = None
        self.send_count = 0

    def send(self, reg):
        self.send_buffer.append(self.state[reg])
        self.send_count += 1

    def evaluate(self, value: int | str) -> int:
        if isinstance(value, int):
            return value
        else:
            return self.state[value]

    def run_until(self):
        # Debug
        run_overrides = True
        breakpoint = None
        # end debug

        while True:
            if self.program_counter == breakpoint:
                print(self.state)
                exit(0)

            if run_overrides:
                match self.program_counter:
                    case 4:
                        if self.state['i'] > 0:
                            # mul a 2  <------+
                            # add i -1        |
                            # jgz i -2 -------+
                            # (if i > 0, a *= 2^i, i=0)
                            self.state['a'] *= 2**self.state['i']
                            self.state['i'] = 0
                            self.program_counter = 7
                            continue
                    case 10:
                        # mul p 8505      <---+
                        # mod p a             |
                        # mul p 129749        |
                        # add p 12345         |
                        # mod p a             |
                        # set b p             |
                        # mod b 10000         |
                        # snd b               |
                        # add i -1            |
                        # jgz i -9        ----+
                        # defaultdict(<class 'int'>, {'p': 1986897071, 'i': 0, 'a': 2147483647, 'b': 7071})
                        if self.state['i'] > 0:
                            a = self.state['a']
                            p = self.state['p']
                            for i in range(self.state['i']):
                                p = (((p * 8505) % a) * 129749 + 12345) % a
                                b = p % 10_000
                                self.send_buffer.append(b)
                            self.state['p'] = p
                            self.state['b'] = b
                            self.state['i'] = 0
                            self.program_counter = 20
                            continue
                    case 27:
                        print(f"Looping with queue of {len(self.receive_buffer)}")
                        p = -self.state['a'] + self.state['b']
                        self.state['p'] = p
                        if p > 0:
                            self.send('b')
                            self.state['f'] = 1
                        else:
                            self.send('a')
                            self.state['a'] = self.state['b']
                        self.state['i'] -= 1
                        self.program_counter = 37
                        continue

            instruction = self.program[self.program_counter]
            match instruction[0]:
                case "snd":
                    self.send(instruction[1])
                case "set":
                    self.state[instruction[1]] = self.evaluate(instruction[2])
                case "add":
                    self.state[instruction[1]] += self.evaluate(instruction[2])
                case "mul":
                    self.state[instruction[1]] *= self.evaluate(instruction[2])
                case "mod":
                    self.state[instruction[1]] %= self.evaluate(instruction[2])
                case "rcv":
                    if len(self.receive_buffer) > 0:
                        self.state[instruction[1]] = self.receive_buffer.pop(0)
                    else:
                        return
                case "jgz":
                    if self.evaluate(self.state[instruction[1]]) > 0:
                        self.program_counter += self.evaluate(instruction[2])
                        continue
            self.program_counter += 1

def part2(parsed):
    a = Machine(parsed, 0)
    b = Machine(parsed, 1)
    a.receive_buffer = b.send_buffer
    b.receive_buffer = a.send_buffer
    while True:
        print(a.send_count, b.send_count)
        a.run_until()
        b.run_until()
        if len(a.send_buffer) == 0 and len(b.send_buffer) == 0:
            return b.send_count

test_input = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
test_parsed = parse(test_input)

def test_part1():
    result = part1(test_parsed)
    assert result == 4, result

def test_part2():
    part2_test = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
    result = part2(parse(part2_test))
    assert result == 3, result

filename = "day18.txt"
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
