from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    # Part one.

    # horizontals
    p1 += sum(row.count('XMAS') + row.count('SAMX') for row in input)

    # verticals 
    p1 += sum(row.count('XMAS') + row.count('SAMX') for row in AoC.rotate_cw(input))
    
    # diagonals
    rows, cols = len(input), len(input[0])

    def check_diagonal(r, c, dr, dc, look_for):
        # (with a little help from my ai friend)
        return all(0 <= r + i * dr < rows and \
                   0 <= c + i * dc < cols and \
                   input[r + i * dr][c + i * dc] == look_for[i] for i in range(len(look_for)))

    for r in range(rows):
        for c in range(cols):
            for s in ['XMAS', 'SAMX']:
                p1 += check_diagonal(r, c, 1, 1, s)
                p1 += check_diagonal(r, c, -1, 1, s)

    # Part two.

    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if input[r][c] == 'A':
                p2 += (check_diagonal(r-1, c-1, 1, 1, 'MAS') or \
                      check_diagonal(r-1, c-1, 1, 1, 'SAM')) and \
                      (check_diagonal(r+1, c-1, -1, 1, 'MAS') or \
                      check_diagonal(r+1, c-1, -1, 1, 'SAM'))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 4
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
