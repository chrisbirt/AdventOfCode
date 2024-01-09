from aoc import AoC
import re

def areaShoelaceMethod(input) -> int:

    vertices = []
    pos = (0, 0)
    perimeter, area = 0, 0
    delta = {'R':(1, 0), 'L':(-1, 0), 'U':(0, 1), 'D':(0, -1) }

    for row in input:
        direction, metres, _ = row.split(' ')
        metres = int(metres)
        perimeter += metres
        dx, dy = delta[direction]
        pos = (pos[0] + dx * metres, pos[1] + dy * metres)
        vertices.append(pos)

    area = 0
    for i in range(len(vertices)):
        area -= vertices[i][0]*vertices[(i+1)%len(vertices)][1]
        area += vertices[i][1]*vertices[(i+1)%len(vertices)][0]

    return int((area + perimeter) / 2 + 1)


def swap_instructions(input):

    ret = []
    dig_map = {'0':'R', '1':'D', '2':'L', '3':'U'}

    for i in input:
        _, _, colour = i.split(' ')    
        direction = dig_map[colour[-2]]
        metres = int(colour[2:-2], 16)
        ret += [' '.join([direction, str(metres), colour])]

    return ret


def solve(input):
    p1, p2 = 0, 0

    p1 = areaShoelaceMethod(input)    
    input = swap_instructions(input)
    p2 = areaShoelaceMethod(input)    

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 18
#puzzle_input = AoC.load_puzzle_input(day, 'test_input')  
puzzle_input = AoC.load_puzzle_input(day)  
solve(puzzle_input)
