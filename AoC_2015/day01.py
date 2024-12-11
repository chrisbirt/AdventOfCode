from aoc import AoC
def solve():

    p1, p2, day = 0, 0, 1

    input = AoC.load_puzzle_input(2015, 1, split_lines = False)

    #with open('input01') as f:
    #    input = f. read()

    p1 = sum(1 if i=='(' else -1 for i in input)

    j = 0
    for idx, char in enumerate(input):
        j += 1 if char == '(' else -1
        if j < 0:
            p2 = idx + 1
            break

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()