from aoc import AoC
import re


def get_adjacent_nodes(input, part):

    #  For each (x,y) node in the input, determine its adjacent nodes

    adj_nodes = {}
    delta = [(0, -1, '^'), (0, 1, 'v'), (1, 0, '>'), (-1, 0, '<')]
    max_x, max_y = len(input[0]), len(input)

    for x in range(max_x):
        for y in range(max_y):
            if input[y][x] == '#':
                continue
            for dx, dy, downhill in delta:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < max_x and 0 <= y1 < max_y:
                    i = input[y1][x1]
                    if (part == 1 and ((i == '.') or (i == downhill))) or \
                       (part == 2 and (i != '#')):
                        adj_nodes[(x, y)] = adj_nodes.get((x, y), []) + [(x1, y1)]
    return adj_nodes


def longest_path_p1(start, end, adj_nodes):

    # traverse all possible paths, find the longest valid path

    all_paths = [[start]]
    idx = 0

    while idx < len(all_paths):
        path = all_paths[idx]
        this_node = path[-1]
        for node in adj_nodes[this_node]:
            if node not in path:
                new_path = path[:] + [node]
                all_paths += [new_path]
        idx += 1

    return max([len(p) for p in all_paths if p[-1] == end]) -1


def get_graph(adj_nodes):

    # Get the graph of nodes and edges.  
    # Also apply edge contraction, and determine the weighted value of the edge (the number of steps)
    #
    # eg: the following adjacent nodes:  (0,1), (1,1), (2,1), (3,1)
    #
    # becomes: { (0,1) : [ [(3,1), 3] }

    # Junctions are nodes with more or less than 2 adjacent nodes. (this includes the start and end)
    #
    junctions = [key for key in adj_nodes.keys() if len(adj_nodes[key])!=2]

    graph = {}
    for junction in junctions:
        for next_node in adj_nodes[junction]:
            
            # keep a track of the nodes we've visited to avoid backtracking. It also provides the length of the path.
            visited = [junction]
            
            # If next node isn't a junction, it's a step on the path.
            while next_node not in junctions:
                visited += [next_node]
                next_node = [node for node in adj_nodes[next_node] if node not in visited][0]
            
            # check if this is
            
            graph[junction] = graph.get(junction, []) + [[next_node, len(visited)]]


    return graph


def longest_path_p2(start, end, graph, curr_len=0, max_len=0, visited=[]):
    # do a depth-first search, looking for the longest path
    #
    if start == end: 
        return max(curr_len, max_len)
    
    if start not in visited:
        visited += [start]
        for node, weight in graph[start]:
            max_len = longest_path_p2(node, end, graph, curr_len + weight, max_len, visited)
        visited.remove(start)
    return max_len


def solve(input):

    start = (input[0].index('.'), 0)
    end = (input[-1].index('.'), len(input)-1)

    adj_nodes = get_adjacent_nodes(input, 1)
    p1 = longest_path_p1(start, end, adj_nodes)
    print(f'Day {day}, part one: {p1}')

    adj_nodes = get_adjacent_nodes(input, 2)
    graph = get_graph(adj_nodes)
    p2 = longest_path_p2(start, end, graph)
    print(f'Day {day}, part two: {p2}')


day = 23
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)

