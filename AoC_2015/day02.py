def solve():

    p1, p2, day = 0, 0, 2

    with open('input02') as f:
        input = f.read().splitlines()

    boxes = [[int(i) for i in r.split('x')] for r in input]

    for b in boxes:
        x, y, z = b
        sides = [2*x*y, 2*y*z, 2*z*x]

        p1 += int(sum(sides) + min(sides)/2)
        p2 += 2 * (sum(b) - max(b)) + x*y*z

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()