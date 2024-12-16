from aoc import AoC
import copy
from collections import defaultdict

# Solve using https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

def solve(input):

    p1, p2 = 0, 0
    sr, sc = 0, 0
    end = ()
    steps = defaultdict(list)
    paths = []
    best_paths = []
    step_points = {}

    # Build a dictionary of steps

    for r in range(len(input)):
        for c in range(len(input[0])):

            if input[r][c] == 'S':
                # Starting position. Initialise the paths
                paths.append(['e', 0, [(r, c)]])

            if input[r][c] == 'E':
                end = (r, c)

            if input[r][c] != '#':
                for d, nr, nc in [('n', r-1, c), ('s', r+1, c), ('e', r, c+1), ('w', r, c-1)]:
                    if 0 <= r < len(input) and 0 <= c <= len(input[0]) and input[nr][nc] !='#':
                        steps[(r, c)].append((d, nr, nc))

    idx = 0
    while idx < len(paths):

        path = paths[idx]
        d, s, prior_steps = path
        r, c = prior_steps[-1]

        # Have we got here in fewer points than any other path? If not, don't bother continuing
        if not (d, r, c) in step_points or step_points[(d, r, c)] >= s:

            step_points[(d, r, c)] = s

            if (r, c) == end:
                best_paths.append(path)
            else:

                for step in steps[(r, c)]:
                    ns = s
                    nd, nr, nc = step

                    if (nr, nc) not in prior_steps:

                        ns += 1 if nd == d else 1001
                        paths.append([nd, ns, prior_steps + [(nr, nc)]])
        idx +=1

    points = sorted([bp[1] for bp in best_paths])

    p1 = points[0]
    p2 = len(set([step for bp in best_paths if bp[1]==p1 for step in bp[2]]))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 16
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)
