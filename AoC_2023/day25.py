from aoc import AoC
import re
import random

# solving day 25 using https://en.wikipedia.org/wiki/Karger%27s_algorithm to find minimum cuts

def get_edges(input):

    # Translate the row input into the vertices and edges of the graph that it represents
    # eg:       jqt: rhn xhk nvd
    # becomes:  ('jqt', 'rhn'), ('jqt', 'xhk'), ('jqt', 'nvd')

    edges = []

    for row in input:
        v1, all_v2s = row.split(': ')
        all_v2s = all_v2s.split(' ')
        edges += [(v1, v2) for v2 in all_v2s]

    return edges


def minimum_cut(edges):

    # Edge contraction. Pick a random edge, and combine the 2 vertices at the end of the edge.
    # Repeat, until we have just two vertices left. Count the number of edges between the 2 vertices.
    # We pick edges at random, hence, the outcome is not deterministic. 
    # This function will be called over and over until it returns a solution with 3 cuts

    vertices = len(set([v for e in edges for v in e]))

    # loop round until we're only left with 2 vertices
    while vertices > 2:
            
        idx = 0
        vertices -= 1

        # Pick a random edge, and create a new vertex, catenating the names of the 
        # other vertices to be the name of the new vertex.
        #
        v1, v2 = edges[random.randint(0, len(edges)-1)]
        v3 = v1 + v2    

        # Replace all occurrances of the two vertices with the new vertex.
        # If an edge ends up with the same vertex at each end, remove it
        #
        while idx < len(edges):
            ev1, ev2 = edges[idx]

            if ev1 in [v1, v2]: 
                ev1 = v3
                edges[idx] = (ev1, ev2)

            if ev2 in [v1, v2]: 
                ev2 = v3
                edges[idx] = (ev1, ev2)

            if ev1 == ev2:
                edges.remove(edges[idx])
            else:
                idx += 1

    # when we get here, we will have two vertices, with a number of edges between them
    #
    min_cut = len(edges)

    # This is a bit of a hack. We have been catenating the vertex names, 
    # and they're all 3 chars long, so we can infer the number of 
    # vertices on each side of the cut from the length of the names.
    #
    v_left, v_right = int(len(edges[0][0])/3), int(len(edges[0][1])/3)
    
    return min_cut, v_left, v_right


def solve(input):

    p1, p2 = 0, 0
    min_cut, v_left, v_right = 0, 0, 0
    attempts = 0

    edges = get_edges(input)

    while min_cut != 3:
        min_cut, v_left, v_right = minimum_cut(edges[:])
        attempts += 1
        print(f'Part 1 attempt {attempts}: min_cut={min_cut}, vertex_counts=({v_left}, {v_right}), part_1={v_left * v_right}')

    p1 = int(v_left * v_right)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 25
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)


