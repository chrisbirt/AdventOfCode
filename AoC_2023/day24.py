from aoc import AoC
import re
import sympy


def parse_input(input):

    rows = []

    # Reformat the input into a list. Also determine the values of m and c in the form y=mx+c
    #
    # eg:      19, 13, 30 @ -2,  1, -2
    # becomes: [19, 13, 30, -2, 1, -2, -0.5, 22.5]   [x, y, z, dx, dy, dz, m, c]]
    #
    for row in input:
        r = [int(i) for i in re.split(', | @ ', row)]
        rows += [r + [ r[4]/r[3], r[1] - (r[4]/r[3] * r[0])]]

    return rows


def intersect(a, b):

    # Return 1 if they intersect in the test area, else 0

    ax, ay, az, adx, ady, adz, am, ac = a
    bx, by, bz, bdx, bdy, bdz, bm, bc = b

    # Are the lines parallel? They'll never cross.
    #
    if am == bm:
        return 0

    # Calculate where they intersect.
    #
    x = (ac - bc) / (bm - am)
    y = am * x + ac

    # Do they intersect in the range?
    #
    if 2 != len([i for i in [x, y] if 200000000000000 <= i <= 400000000000000]):
        return 0    

    # Did they cross in the past? Check the direction of travel.
    #
    if ((x - ax) * adx < 0) | ((x - bx) * bdx < 0):
        return 0

    if ((y - ay) * ady < 0) | ((y - by) * bdy < 0):
        return 0

    return 1


def part_two(input):

    # NOT all my own work. Found a solution that uses sympy to solve the simultaneous equations.

    x, y, z, dx, dy, dz = sympy.symbols("x, y, z, dx, dy, dz")

    equations = []

    for i, (ix, iy, iz, idx, idy, idz, _, _) in enumerate(input):
        equations.append((x-ix)*(idy-dy)-(y-iy)*(idx-dx))
        equations.append((y-iy)*(idz-dz)-(z-iz)*(idy-dy))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(j % 1 == 0 for j in soln.values())]
        if len(answers) == 1:
            return answers[0][x] + answers[0][y] + answers[0][z]

    return 0


def solve(input):

    p1, p2 = 0, 0
    input = parse_input(input)

    for a in range(len(input)):
        for b in range(a+1, len(input)):
            p1 += intersect(input[a], input[b])

    p2 = part_two(input)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 24
puzzle_input = AoC.load_puzzle_input(day, 'input')
solve(puzzle_input)
