from aoc import AoC
import re


def solve(input):
    p1, p2 = 0, 0

    l, r = zip(*[map(int, re.split('   ', row)) for row in input])
    l, r = sorted(l), sorted(r)

    p1 = sum(abs(l[i] - r[i]) for i in range(len(l)))
    p2 = sum(i * r.count(i) for i in l)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 1
puzzle_input = AoC.load_puzzle_input(day, True)
solve(puzzle_input)

puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
