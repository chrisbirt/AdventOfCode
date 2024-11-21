from aoc import AoC
import re

def slide_rocks(grid):   
    # slides the rocks all to the left
    for i, r in enumerate(grid):
        while '.O' in r:
            m = re.search('\.{1,}O', r)
            r = r[:m.start()] + r[m.start():m.end()].replace(m.group(), m.group()[::-1]) + r[m.end():]
        grid[i] = r
    return grid

def solve(input):
    p1, p2 = 0, 0

    # we are going to orientate as follows:
    #     E
    #  N <-- S 
    #     W
    #
    # just a bit easier to work with rows than columns
    
    # Part one. Rotate input to the left (so N is oriented left), slide rocks to the left, then rotate grid to the right to sum up the answer.
    #
    grid = AoC.rotate_ccw(input)
    grid = slide_rocks(grid)
    grid = AoC.rotate_cw(grid)
    p1 = sum(row.count('O') * (len(grid) - idx) for idx, row in enumerate(grid))

    # Part two.
    # For simplicity, rotate the input 180 degrees, so that the first rotate right will place the top of the grid in the N position, on the left.
    #
    grid = AoC.rotate_cw(input, 2)

    cycles = 1000000000
    grid_states = [input]

    # Running a billion cycles takes too long. After a time, there must be some repetition in the cycles. Find that, and use it to
    # extrapolate the grid for the billionth cycle.
    #
    for _ in range (cycles):
        for _ in range(4):
            grid = slide_rocks(AoC.rotate_cw(grid))
        try:
            match_idx = grid_states.index(grid)
            repeat = len(grid_states) - match_idx
            grid = grid_states[cycles - int((cycles-match_idx)/repeat) * repeat]
            break
        except:
            grid_states.append(grid)

    # Again, spin 180 degrees so North is top.
    #
    grid = AoC.rotate_cw(grid, 2)
    p2 = sum(row.count('O') * (len(grid) - idx) for idx, row in enumerate(grid))        

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 14
puzzle_input = AoC.load_puzzle_input(day)  
solve(puzzle_input)
