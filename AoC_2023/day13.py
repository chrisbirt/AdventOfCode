from aoc import AoC
import re

def find_mirror_index(pattern, diff):

    # Compare each row with the next for any differences.
    # for part 1, diff = 0, for part 2, diff = 1 (ie, just one difference)
    
    for y in range(len(pattern)-1):

        diffs = 0
    
        # compare this row to the next one, then the prior row to the next+1 etc until we hit a boundary
        #
        prior, next = y, y + 1
        while 0 <= prior < next < len(pattern):
            
            # compare each character in the two rows. Keep a count of any differences
            #
            for x in range(len(pattern[0])):
                diffs += 1 if (pattern[prior][x] != pattern[next][x]) else 0

            prior, next = prior - 1, next + 1

        # we've compared all the prior/next rows around the current row (y).
        # if we have the right number of differences, return the row number
        #
        if diffs == diff:
            return y + 1
        
    return 0

def flip_row_cols(pattern):

    # utility function that flips a 2 dimensional list
    #
    # eg:  [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]   becomes: [ [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    #
    cols = []
    for x in range(len(pattern[0])):
        cols.append(''.join(pattern[y][x] for y in range(len(pattern))))
    return cols

def solve(input):
    p1, p2 = 0, 0

    patterns = [i.splitlines() for i in input.split('\n\n')]

    for p in patterns:

        p_flip = flip_row_cols(p)

        # part 1  
        p1 += find_mirror_index(p, 0) * 100 + find_mirror_index(p_flip, 0)

        # part 2        
        p2 += find_mirror_index(p, 1) * 100 + find_mirror_index(p_flip, 1)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 13
#puzzle_input = AoC.load_puzzle_input(day, 'test_input', split_lines = False)
puzzle_input = AoC.load_puzzle_input(day, split_lines = False)
solve(puzzle_input)
