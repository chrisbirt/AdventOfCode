from aoc import AoC
import re
import numpy as np

def solve(input):

    p1, p2 = 0, 0

    idx = 0
    results = []

    for row in input:

        _, wins, nums = re.split(': | \| ', row)
        wins = [int(x) for x in re.split('  | ', wins.strip())]
        nums = [int(x) for x in re.split('  | ', nums.strip())]

        x = list(set(wins).intersection(nums))

        # Store the number of matches, calculate the number of points scored, and (for part 2) number of copies (defaulted to 1)
        #
        results.append([len(x), pow(2, len(x)-1) if x else 0, 1])
    
    p1 = sum([n[1] for n in results])

    # Part two. For each result row, increment the number of copies for subsequent rows.
    #
    for idx, row in enumerate(results):
        for n in results[idx + 1 : idx + row[0] + 1]:
            n[2] += row[2]

    p2 = sum([n[2] for n in results])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 4
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)