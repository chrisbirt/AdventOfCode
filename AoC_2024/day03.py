from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    # Part one.

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    p1 = sum(int(l) * int(r) for l, r in matches)

    # Part two.

    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    on_off = True

    matches = re.findall(pattern, input)
    for m in matches:
        if m == 'do()':
            on_off = True
        elif m == "don't()":
            on_off = False
        elif on_off:
            # mul(554,894) format and on_off is on.
            l, r = map(int, m[4:-1].split(','))
            p2 += l * r

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 3
puzzle_input = AoC.load_puzzle_input(day,split_lines=False)
solve(puzzle_input)
