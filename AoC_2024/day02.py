from aoc import AoC
import re

def is_valid_report(r):

    # Use the first and second levels in the report to determine whether they are
    # ascending or descending.
    #
    direction = r[1] - r[0]

    # Check that all the steps between levels are between 1 and 3, and that they are in the
    # same direction as the first pair.
    # 
    # Original code:
    #
    # for i in range(len(r)-1):
    #     step = r[i+1] - r[i]
    #     if 1 <= abs(step) <= 3:
    #         if (direction * step) < 0:
    #             return False
    #     else:
    #         return False
    # return True
    #
    # Copilot optimised code:
    #
    return all(1 <= abs(step := r[i + 1] - r[i]) <= 3 and direction * step >= 0 for i in range(len(r) - 1))


def solve(input):
    p1, p2 = 0, 0

    reports = [[int(i) for i in row.split(' ')] for row in input]

    # Part one.
    
    p1 = sum(is_valid_report(r) for r in reports)

    # Part two.

    for r in reports:
        ok = is_valid_report(r) or any(is_valid_report(r[:i] + r[i+1:]) for i in range(len(r)))
        if ok:
            p2 += 1

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 2
puzzle_input = AoC.load_puzzle_input(day, True)
#solve(puzzle_input)

puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
