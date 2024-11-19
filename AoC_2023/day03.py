from aoc import AoC
import re
import numpy as np

def solve(input):

    p1, p2 = 0, 0

    all_nums, all_symbols = [], []

    for idx, row in enumerate(input):

        # Find all the numbers. (Look for sets of adjacent digits in the row).
        #
        nums = re.finditer(r'\d+', row)

        # Store the number, it's x(start), x(end) and y positions.
        #
        all_nums += [(int(match.group()), match.start(), match.start() + len(match.group())-1, idx) for match in nums]

        # Find all the symbols. (Look for non-digit, non-period symbols in the row).
        #
        symbols = re.finditer(r'[^0-9.]+', row)

        # Store the symbol, it's x and y positions.
        #
        all_symbols += [(match.group(), match.start(), idx) for match in symbols]

    # For each symbol, find all adjacent numbers.
    # The symbol is adjacent if:
    #  - it's x value is between the numbers x(start) - 1 and the numbers x(end) + 1
    #  - it's y value is equal to the numbers y value + or - 1
    #
    for s in all_symbols:
        adj_nums = [n[0] for n in all_nums if (n[1]-1 <= s[1] <= n[2]+1) & (n[3]-1 <= s[2] <= n[3]+1)]

        # Part one. Sum all the adjacent numbers
        #
        p1 += sum(adj_nums)

        # Part two. if there are two adjacent numbers and the symbol is a '*', the multiply the numbers.
        #
        if (len(adj_nums) == 2) & (s[0]=='*'):
            p2 += np.prod(adj_nums)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 3
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)