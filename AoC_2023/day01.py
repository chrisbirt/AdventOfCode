from aoc import AoC
import re

def solve(input):

    p1, p2 = 0, 0

    nums  = [['1', 'one'],   ['2', 'two'],   ['3', 'three'], 
             ['4', 'four'],  ['5', 'five'],  ['6', 'six'], 
             ['7', 'seven'], ['8', 'eight'], ['9', 'nine']]
 
    for row in input:

        # Part one. 
        #
        # Extract a list of the digits in the row, then catenate the first and last digits
        #
        digits = re.findall(r'\d', row)
        if digits:
            p1 += int(digits[0]+digits[-1])
 
        # Part two.
        #
        # Extract a list of the digits, or the digit equivalent of a number string
        #
        digits = []

        for i in range(len(row)):
            for n in nums:
                if row[i] == n[0] or row[i:].startswith(n[1]):
                    digits.append(n[0])

        if digits:
            p2 += int(digits[0]+digits[-1])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 1
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)


