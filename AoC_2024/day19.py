from aoc import AoC

def solve(input):
    p1, p2 = 0, 0

    towels = input[0].split(', ')
    designs = input[2:]

    cache = {}


    def match_design(d):

        if d in cache:
            return cache[d]
        
        if len(d) == 0:
            return 1
        
        ret = 0
        for t in towels:
            if d.startswith(t):
                nd = d[len(t):]
                cache[nd] = match_design(nd)
                ret += cache[nd]
        
        return ret


    results = [match_design(d) for d in designs]
    p1 = len([r for r in results if r > 0])
    p2 = sum(results)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 19
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)
