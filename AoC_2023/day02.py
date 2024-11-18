from aoc import AoC
import re
import numpy as np

def solve(input):

    p1, p2 = 0, 0

    # loop round each game in the input
    #
    for row in input:

        game, cubes = row.split(':')

        # For each cube colour, the list holds the max number expected, 
        # and the actual number (defaulted to zero)
        #
        cube_limits = [['red', 12, 0], ['green', 13, 0], ['blue', 14, 0]]

        # Identify the game number
        #
        id = int(game.split(' ')[1])

        # Reformat the cubes data into a list of all cube counts
        #
        cubes = re.split('; |, ', cubes)
        cubes = [c.split() for c in cubes]

        # For each cube colour in cube_limits, get the max number of cubes actually picked
        #
        for cl in cube_limits:
            cl[2] = max([int(c[0]) for c in cubes if c[1] == cl[0]])

        # if all the actual cube counts are < the max, then ok
        #        
        #x = len([c for c in cube_limits if c[2] <= c[1]])
        #if len(x) == len(cube_limits):
        #    p1 += game_id

        # Part one. Sum the ids of all legal games
        #
        if all(c[2] <= c[1] for c in cube_limits):
            p1 += id

        # Part two. The power is the product of the max number of each cube found
        #
        p2 += np.prod([c[2] for c in cube_limits])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 2
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
