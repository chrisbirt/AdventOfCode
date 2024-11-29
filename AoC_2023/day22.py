from aoc import AoC
from collections import deque
import re

# Took some help from hyperneutrino for part two, 
#  incl the tip to use dictionaries for tracking the above/below relationships

def find_adjacents(bricks):
    above = {i: set() for i in range(len(bricks))}
    below = {i: set() for i in range(len(bricks))}

    for i, b1 in enumerate(bricks):
        for j, b2 in enumerate(bricks[:i]):
            if is_above(b1, b2, True):
                above[j].add(i)
                below[i].add(j)
    
    return above, below


def is_above(b1, b2, ontop=False):
    
    # Check if the bricks overlap in the x plane and y plane.
    # Also check if it's above/on top in the z plane.
    #            
    return (max(b1[0], b2[0]) <= min(b1[3], b2[3])) and \
           (max(b1[1], b2[1]) <= min(b1[4], b2[4])) and \
           ((not ontop and b1[2] > b2[5]) or (ontop and b1[2] == b2[5] + 1))


def settle_bricks(bricks):

    # Ensure the bricks are ordered in ascending order in the z plane.
    #
    bricks.sort(key= lambda brick: brick[5])

    for i, b1 in enumerate(bricks):
        # Assume the brick settles on the floor; unless one of the prior bricks is beneath it...
        #
        z = 1   
        for j, b2 in enumerate(bricks[:i]):
            if is_above(b1, b2):
                z = max(z, b2[5] + 1)
        b1[5] = b1[5] - b1[2] + z
        b1[2] = z

    # and re-sort the bricks (since they may have landed at different heights)
    #
    bricks.sort(key= lambda brick: brick[5])
    return bricks


def solve(input):
    p1, p2 = 0, 0

    bricks = [list(map(int, re.split('~|,', i))) for i in input]
    bricks = settle_bricks(bricks)

    # build a 2-way map
    #
    bricks_above, bricks_below = find_adjacents(bricks)

    # Part one. For each brick, check if all the bricks above it have more than one brick below themselves
    #
    for i in range(len(bricks)):
        if all(len(bricks_below[ba]) > 1 for ba in bricks_above[i]):
            p1 +=1

    # Part two.
    #
    for i in range(len(bricks)):

        # initialise a queue of bricks above i, where the bricks above that only have one below them
        #
        q = deque(j for j in bricks_above[i] if len(bricks_below[j]) == 1)

        # Hold a set of the bricks toppled
        #
        toppled = set(q)
        toppled.add(i)
        
        while q:
            b1 = q.popleft()
            for b2 in (bricks_above[b1] - toppled):     # don't repeat any brick already toppled
                if bricks_below[b2] <= toppled:         # subset operation here. if everything beneath b2 is in the set of bricks already toppled, then...
                    q.append(b2)                        # b2 is no longer supported, so add it to the q.
                    toppled.add(b2)                     # also add it to the list of toppled bricks
        
        p2 += len(toppled) - 1                          # subtract the starting brick, since it wasn't toppled as such.

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 22
puzzle_input = AoC.load_puzzle_input(day, 'input')
solve(puzzle_input)
