from aoc import AoC
import re

# There must be a cleverer way of doing this, as a function of the coordinates of the obstacles
# but for now, everything is brute-force.
#
# This also needs refactoring - a lot!

def solve(input):
    p1, p2 = 0, 0
    gr, gc = 0, 0
    visited = set()

    # find the guard
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == '^':
                gr, gc = r, c

    # he's moving upwards
    dr, dc = -1, 0
    
    while True:
        visited.add((gr, gc))

        # is he about to step off the map? We're done.
        if (gr + dr < 0) or (gr + dr) >= len(input) or \
           (gc + dc < 0) or (gc + dc) >= len(input[0]):
            break

        # is he about to walk into an obstacle? Change direction.
        if input[gr+dr][gc+dc] == '#':
            i = dc
            dc = -dr
            dr = i

        # take a step.
        gr += dr
        gc += dc

    p1 = len(visited)
 
    # Part two.

    # Made a function of part one. Add an obstacle and see if it loops.

    def in_a_loop(input):

        visited = set()

        # find the guard
        for r in range(len(input)):
            for c in range(len(input[0])):
                if input[r][c] == '^':
                    gr, gc = r, c

        # he's moving upwards
        dr, dc = -1, 0
    
        while True:
            #have we already been here? We're in a loop
            if (gr, gc, dr, dc) in visited:
                return True
            
            visited.add((gr, gc, dr, dc))   # also track direction

            # is he about to step off the map? We're done - NOT in a loop
            if (gr + dr < 0) or (gr + dr) >= len(input) or \
            (gc + dc < 0) or (gc + dc) >= len(input[0]):
                break

            # is he about to walk into an obstacle? Change direction.
            if input[gr+dr][gc+dc] == '#':
                i = dc
                dc = -dr
                dr = i
            else:            
                # take a step.
                gr += dr
                gc += dc

        return False

    for r in range(len(input)):
        for c in range(len(input[0])):
            input2 = input[:]
            if input2[r][c] != '^':
                input2[r] = input2[r][:c] + '#' + input2[r][c+1:]
                p2 += in_a_loop(input2)


    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 6
puzzle_input = AoC.load_puzzle_input(day, test_file = False)
solve(puzzle_input)
