from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    # eg. p=69,74 v=68,-98  becomes [69, 74, 68, -98]

    input = [[int(r) for r in row] for row in (row.replace('p=', '').replace(' v=', ',').split(',') for row in input)]

    rows = 103
    cols = 101 
    secs = 100

    locs = []

    for c, r, dc, dr in input:
        nr = (r + dr * secs) % rows
        nc = (c + dc * secs) % cols
        locs.append((nr, nc))

    xr = (rows // 2) 
    xc = (cols // 2) 

    p1 = len([l for l in locs if l[0] < xr and l[1] < xc]) * \
         len([l for l in locs if l[0] > xr and l[1] < xc]) * \
         len([l for l in locs if l[0] < xr and l[1] > xc]) * \
         len([l for l in locs if l[0] > xr and l[1] > xc]) 

    # Part two.

    # A bit of guesswork here. I thought maybe the centre vertical line was a line of reflection for the xmas tree, but code 
    # never returned. Then found that counting the number of robots in each quadrant yielded a point in time with a quadrant
    # with loads of robots in it.
    

    max_q = 0

    for sec in range(100000):

        locs = []

        for c, r, dc, dr in input:
            nr = (r + dr * sec) % rows
            nc = (c + dc * sec) % cols
            locs.append((nr, nc))

        q1 = len([l for l in locs if l[0] < xr and l[1] < xc])
        q2 = len([l for l in locs if l[0] > xr and l[1] < xc])
        q3 = len([l for l in locs if l[0] < xr and l[1] > xc])
        q4 = len([l for l in locs if l[0] > xr and l[1] > xc])

        max_q1234 = max([q1, q2, q3, q4])

        if max_q1234 > max_q:
            max_q = max_q1234
            p2 = sec

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 14
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)

