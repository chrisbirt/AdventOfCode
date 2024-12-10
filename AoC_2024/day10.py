from aoc import AoC
from collections import defaultdict

def solve(input):
    p1, p2 = 0, 0

    trails = []
    steps = defaultdict(list)

    input = [[int(x) for x in list(r)] for r in input]

    # Parse the input. Create a dictionary of valid steps, and also find the trailheads
    for r in range(len(input)):
        for c in range(len(input[0])):

            # It's a trailhead. Add to the list of trails.
            if input[r][c] == 0:
                trails.append([(r, c)])

            # find each valid step from here and add to dictionary
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(input) and 0 <= nc < len(input[0]):
                    if input[r][c] + 1 == input[nr][nc]:
                        steps[(r, c)].append((nr, nc))

    i = 0
    while i < len(trails):
        trails += [trails[i] + [step] for step in steps[trails[i][-1]]]
        i += 1

    # get the pairs of locations for the trails that are the right length (visited 0 up to 9)
    pairs = [(trail[0], trail[9]) for trail in trails if len(trail) == 10]
    p1 = len(set(pairs))
    p2 = len(pairs)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 10
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)
