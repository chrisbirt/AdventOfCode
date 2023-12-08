from aoc import AoC
import math
import re

def calc_steps(instructions, start_nodes, nodes, end_regex):

    lr_idx = {'L': 0, 'R': 1}
    steps = []
    
    for node in start_nodes:

        step = 0
        matched = False

        while not matched:
            for lr in instructions:

                step += 1
                node = nodes[node][lr_idx[lr]]

                if re.fullmatch(end_regex, node):
                    steps.append(step)
                    matched = True

    return steps

def solve():
    global puzzle_input
    p1, p2 = 0, 0

    instructions, nodes = puzzle_input.split('\n\n')
    nodes = {n[0:3] : [n[7:10], n[12:15]] for n in nodes.split('\n')}

    start_nodes =['AAA']
    p1 = calc_steps(instructions, start_nodes, nodes, '^ZZZ$')[0]

    start_nodes = [i for i in nodes.keys() if i.endswith('A')]
    p2 = math.lcm(*calc_steps(instructions, start_nodes, nodes, '^..Z$'))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 8
puzzle_input = AoC.load_puzzle_input(day, split_lines=False)
solve()