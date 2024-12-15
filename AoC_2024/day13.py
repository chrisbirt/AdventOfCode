from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    # Split the input text into blocks
    blocks = input.strip().split('\n\n')

    # Initialize an empty list to hold the results
    result = []

    # Process each block
    for block in blocks:
        # Use regular expressions to find the numbers
        numbers = re.findall(r'[+-]?\d+', block)
        # Convert the string numbers to integers and add to the result list
        result.append([int(num) for num in numbers])

    def solve_for_a_b(r, i=0):
        x1, y1, x2, y2, x, y = r
        x += i
        y += i
        det = x1 * y2 - x2 * y1
        a = (y2 * x - x2 * y) / det
        b = (-y1 * x + x1 * y) / det
        return a, b

    for r in result:
        a, b = solve_for_a_b(r)
        if a == int(a) and b == int(b):
            p1 += a*3 + b

    for r in result:
        a, b = solve_for_a_b(r,10000000000000)
        if a == int(a) and b == int(b):
            p2 += a*3 + b

    print(f'Day {day}, part one: {int(p1)}')
    print(f'Day {day}, part two: {int(p2)}')


day = 13
puzzle_input = AoC.load_puzzle_input(day, False, False)
solve(puzzle_input)
