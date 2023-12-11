from aoc import AoC
import re

def find_galaxies(universe):

    galaxies = []

    # search the rows for galaxies. Store the cartesian coordinates.

    for iy, y in enumerate(universe):
        galaxies += [(ix,iy) for ix, x in enumerate(y) if x == '#']

    return galaxies

def expand_universe(galaxies, multiply_by):

    new_galaxies = galaxies[:]

    # firstly, get a distinct list of rows/columns where galaxies are found

    all_ys = set([x[1] for x in galaxies])
    all_xs = set([x[0] for x in galaxies])
    
    for ig, g in enumerate(galaxies):
        
        x, y = g[0], g[1]

        # expand the x/y coordinates by the number of lower x/y coordinates that don't have any galaxies        
        # also multiply the expansion  ( dist-1 is because we already have one gap, so we're appending to the gap. )
        x = x + (x - len([i for i in all_xs if i < x]))*(multiply_by-1)
        y = y + (y - len([i for i in all_ys if i < y]))*(multiply_by-1)

        new_galaxies[ig] = (x,y)
    
    return new_galaxies

def shortest_paths(galaxies):
     
    shortest_paths = []

    # compare each galaxy coordinate with the following coordinates in the list.
    for i in range(len(galaxies)-1):
        gfrom = galaxies[i]

        for j in range(i+1, len(galaxies)):
            gto = galaxies[j]

            # shortest path between two galaxies is the sum of the absolute differences of the x's and the y's
            shortest_paths.append(abs(gfrom[0]-gto[0]) +  abs(gfrom[1]-gto[1]))

    return shortest_paths          

def solve():

    global puzzle_input
    p1, p2 = 0, 0

    galaxies = find_galaxies(puzzle_input)

    new_galaxies = expand_universe(galaxies, 2)
    p1 = sum(shortest_paths(new_galaxies))

    new_galaxies = expand_universe(galaxies,1000000)
    p2 = sum(shortest_paths(new_galaxies))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 11
puzzle_input = AoC.load_puzzle_input(day)
solve()
