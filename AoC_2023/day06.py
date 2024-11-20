from aoc import AoC
import re
import math

def wins(time, distance):
    # we need to solve a quadradic equation
    #
    disc =  math.sqrt((time*time) - 4*(distance+1))
    return 1 + math.floor((time + disc) / 2) - math.ceil((time - disc) / 2)

def solve(input):

    p1, p2 = 1, 0

    # part 1
    times = [int(i) for i in re.findall('\d+', puzzle_input[0])]
    distances = [int(i) for i in re.findall('\d+', puzzle_input[1])]

    for time, distance in zip(times, distances):
        p1 *= wins(time, distance)

    # part 2
    time = int(''.join(re.findall('\d+', puzzle_input[0])))
    distance = int(''.join(re.findall('\d+', puzzle_input[1])))

    p2 = wins(time, distance)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 6
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)