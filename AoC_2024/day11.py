from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    input = [int(i) for i in input.split(' ')]

    # Part two was way too slow. Refactored and introduced caching.

    cache = {}

    def expand_stone(stone, blinks):

        if (stone, blinks) in cache:
            return cache[(stone, blinks)]

        if blinks == 0:
            return 1
        
        ret = 0
        blinks -= 1
        
        if stone == 0:
            ret = expand_stone(1, blinks)
        
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            h = len(s) // 2  # half s
            ret = expand_stone(int(s[:h]), blinks) + expand_stone(int(s[h:]), blinks)
        
        else:
            ret = expand_stone(stone * 2024, blinks)

        cache[(stone, blinks+1)] = ret
        return ret

    for i in input:
        p1 += expand_stone(i, 25)
        p2 += expand_stone(i, 75)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 11
puzzle_input = AoC.load_puzzle_input(day, split_lines=False)
solve(puzzle_input)
