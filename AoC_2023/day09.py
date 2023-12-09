from aoc import AoC
import math
import re

def solve():
    global puzzle_input
    p1, p2 = 0, 0

    ## conveert the input
    #  
    #  eg:  0 3 6 9 12 15        becomes [ [[0, 3, 6, 9, 12, 15]], [[1, 3, 6, 10, 15, 21]] ]
    #       1 3 6 10 15 21
    #     
    puzzle_input = [[[int(x) for x in y.split(' ')]] for y in puzzle_input]

    # Extend each list in the puzzle input, appending a list of the transformations.
    #
    # eg:       [[0, 3, 6, 9, 12, 15]]
    # becomes:  [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]
    #
    for line in puzzle_input:

        # Process until we have list of zeros.
        # Sum up part one along the way. 
        # (the sum of the last elements of each list is the value of the next item in the first list)
        #
        while sum(map(abs, line[-1])) > 0:
            p1 += line[-1][-1]
            line.append([line[-1][i+1]-line[-1][i] for i in range(len(line[-1])-1)])

        # Part two is a function of the first elements in the list a - b + c - d + e ....
        #
        #p2 += line[0][0]
        for i in range(len(line)):
            p2 += line[i][0] * (1 if (i % 2 == 0) else -1)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 9
puzzle_input = AoC.load_puzzle_input(day, test_input=False)
solve()