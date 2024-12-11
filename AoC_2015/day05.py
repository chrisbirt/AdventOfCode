from aoc import AoC

def solve():

    year, day = 2015, 5
    input = AoC.load_puzzle_input(year, day)
    p1, p2, = 0, 0

    disallowed = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']

    for z, i in enumerate(input):
        r1 = sum(i.count(v) for v in vowels) >= 3
        r2 = sum(i.count(d) for d in disallowed) == 0
        r3 = any(i[j] == i[j+1] for j in range (len(i) - 1))
        p1 += (r1 and r2 and r3)

        r4 = any(i[j:j+2] in i[j+2:] for j in range(len(i) - 1))
        r5 = any(i[j] == i[j+2] for j in range (len(i) - 2))
        p2 += (r4 and r5)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()