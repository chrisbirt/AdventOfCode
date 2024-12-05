from aoc import AoC
import functools


def solve(input):
    p1, p2 = 0, 0

    orderings, updates = input.split('\n\n')
    orderings = [o.split('|') for o in orderings.splitlines()]
    updates = [u.split(',') for u in updates.splitlines()]

    # use a custom comparison function. Also used for sort in part 2
    def compare(l, r):
        if l == r:
            return 0
        if any(o for o in orderings if o == [r, l]):
            return 1
        return -1


    for u in updates:
        ok = True
        for i in range(len(u)):
            for j in range(i+1, len(u)):
                if compare(u[i], u[j]) == 1:
                    ok = False
                    break
        if ok:
            # Part one.
            p1 += int(u[len(u) // 2])
        else:
            # Part two. Custom sort like Aoc2023 day 7
            u = sorted(u, key=functools.cmp_to_key(compare))
            p2 += int(u[len(u) // 2])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 5
puzzle_input = AoC.load_puzzle_input(day, split_lines=False, test_file=False)
solve(puzzle_input)
