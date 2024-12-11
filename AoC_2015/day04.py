from aoc import AoC
import hashlib

def findhash(input, prefix):

    ret = 0
    hash = ''

    while not hash.startswith(prefix):
        ret += 1
        hash = hashlib.md5 ((input + str(ret)).encode('utf-8')) .hexdigest()

    return ret


def solve():

    year, day = 2015, 4
    p1, p2, = 0, 0
    hash = ''

    input = AoC.load_puzzle_input(year, day, split_lines = False)

    p1 = findhash(input, '00000')
    p2 = findhash(input, '000000')

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()