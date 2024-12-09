from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    antennae = {}

    for r, row in enumerate(input):
        for c, ref in enumerate(row):
            if ref != '.':
                antennae.setdefault(ref, []).append((r, c))

    # Part one.

    def calc_antinodes(antennae, repeat=False):
    
        dr, dc = 0, 0
        ret = []

        for i, a1 in enumerate(antennae):
            for j, a2 in enumerate(antennae): # comparing each pair twice, in different directions
                if i != j:
                    dr, dc = (a2[0] - a1[0]), (a2[1] - a1[1])
    
                    # evaluate antinode in one direction only, since the other direcion will be evaluated with the reversed pair
                    ret += [(a2[0] + dr, a2[1] + dc)]
                    
                    r = 0
                    while repeat:
                        rx, cx = (a2[0] + (r * dr)), (a2[1] + (r * dc))
                        if 0 <= rx < len(input) and 0 <= cx < len(input[0]):
                            ret += [(rx, cx)]
                            r += 1
                        else:
                            break
 
        # Filter out any coords off the map
        return [a for a in ret if 0 <= a[0] < len(input) and 0 <= a[1] < len(input[0])]

    p1 = len(set([antinodes for v in antennae.values() for antinodes in calc_antinodes(v)]))
    p2 = len(set([antinodes for v in antennae.values() for antinodes in calc_antinodes(v, True)]))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 8
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
