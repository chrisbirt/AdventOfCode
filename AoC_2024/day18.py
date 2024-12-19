from aoc import AoC
from collections import defaultdict

def solve(input):
    p1, p2 = 0, 0

    def calc_path(size, as_at, input):
        size += 1
        adjacents = defaultdict(list)
        corrupts = [(int(c[0]), int(c[1])) for c in [r.split(',') for r in input[:as_at]]]

        # build a dictionary of adjacents

        for x in range(size):
            for y in range(size):
                for nx, ny in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < size and 0 <= ny < size:
                        if (nx, ny) not in corrupts:
                            adjacents[(x, y)].append((nx, ny))    

        # now find shortest path 

        start = (0,0)
        end = (size-1, size-1)

        paths = [[start]]
        visited = []
        
        idx = 0
        while idx < len(paths):

            path = paths[idx]
            step = path[-1]

            visited.append(step)

            for adj in adjacents[step]:
                if adj not in visited:

                    visited.append(adj)
                    paths.append(path + [adj])

                    if adj == end:
                        return(len(path))

            idx += 1

        return 0

    p1 = calc_path(70, 1024, input)

    print(f'Day {day}, part one: {p1}')

    # Part two

    # implement a binary search here to try and find the offending block

    left, right = 1023, len(input) - 1

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if left == right:
            p2 = input[mid-1]
            break
        elif calc_path(70, mid, input) > 0:
            left = mid + 1
        else:
            right = mid - 1

    print(f'Day {day}, part two: {p2}')


day = 18
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
