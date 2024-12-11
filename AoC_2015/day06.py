from aoc import AoC
import numpy as np
import re

def solve():

    year, day = 2015, 6
    input = AoC.load_puzzle_input(year, day)
    p1, p2, = 0, 0

    lights_p1, lights_p2 = np.zeros((1000,1000)), np.zeros((1000,1000))

    for row in input:
        action, x1, y1, _, x2, y2 = re.split(' |,', row.replace(' o', 'o'))
        x1, y1, x2, y2 = [int(i) for i in [x1, y1, x2, y2]]
        x2 += 1
        y2 += 1 
        if action == 'toggle':
            lights_p1[y1:y2, x1:x2] = 1 - lights_p1[y1:y2, x1:x2]
            lights_p2[y1:y2, x1:x2] = 2 + lights_p2[y1:y2, x1:x2]
        
        elif action == 'turnon':
            lights_p1[y1:y2, x1:x2] = 1
            lights_p2[y1:y2, x1:x2] = lights_p2[y1:y2, x1:x2] + 1

        elif action  == 'turnoff':
            lights_p1[y1:y2, x1:x2] = 0
            lights_p2[y1:y2, x1:x2] = np.maximum(lights_p2[y1:y2, x1:x2] - 1, 0)
        
        else:
            print('invalid action:', action)

    p1 = int(lights_p1.sum())
    p2 = int(lights_p2.sum())

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()