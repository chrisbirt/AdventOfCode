from aoc import AoC

def solve():

    year, day = 2015, 3
    p1, p2, = 0, 0
    delta = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0,-1)}

    input = AoC.load_puzzle_input(year, day, split_lines = False)

    visited = [(0,0)]
    for char in input: 
        visited.append(tuple(map(sum, zip(delta[char], visited[-1]))))
        
    p1 = len(set(visited))

    visited, robovisited = [(0,0)], [(0,0)]

    for idx, char in enumerate(input): 
        if idx % 2 == 0: 
            visited.append(tuple(map(sum, zip(delta[char], visited[-1])))) 
        else: 
            robovisited.append(tuple(map(sum, zip(delta[char], robovisited[-1]))))
    
    p2 = len(set(visited + robovisited))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()