from aoc import AoC
import re

def adjacent_pipes(coord):
    global puzzle_input
    
    # find all the adjacent pipes (up/down/left/right) that can be moved to from the current pipe
    
    adj_pipes = []

    for delta in [(0, 1),'|JL'], [(0, -1),'|F7'], [(1, 0),'-J7'], [(-1, 0),'-FL']:

        next_x = coord[0] + delta[0][0]
        next_y = coord[1] + delta[0][1]

        # check we're still on the map (x axis)
        if 0 <= next_x <= len(puzzle_input[0]) - 1:

            # check we're still on the map (y axis)
            if 0 <= next_y <= len(puzzle_input) - 1:

                # see if the next piece of pipe is one we can move to
                if puzzle_input[next_y][next_x] in delta[1]:

                    adj_pipes.append((next_x, next_y))

    return adj_pipes

def get_path(adj_positions, start_position):
   
    # maintain a list of all paths. each path is itself a list
    all_paths = [[start_position]]
    
    # keep a list of visited positions, so we don't end up going back/forwards infinately
    previous_positions = [start_position]

    path_idx = 0
    while path_idx < len(all_paths):
        
        path = all_paths[path_idx]
        this_position = path[-1]
        next_positions = adj_positions[this_position]

        for next_position in next_positions:
           if not next_position in previous_positions:
                new_path = path[:]
                new_path.append(next_position)
                all_paths.append(new_path)
                previous_positions.append(next_position)

        path_idx += 1
        
    return all_paths[-2] + all_paths[-1][1:]
        
def solve():
    global puzzle_input
    p1, p2 = 0, 0

    adj_pipes = {}
    start_position = None

    # scan the entire pipe map, pipe piece by pipe piece, identifying 
    # the pieces that can be moved to. Create a dictionary.
    # also capture the position of 'S', so we know where to start walking from

    # for each row:
    for y in range(len(puzzle_input)):

        # for each character in row:
        for x in range(len(puzzle_input[0])):
            
            # capture start position
            if puzzle_input[y][x] == 'S':
                start_position = (x,y)

            # add adjacent pipes to the dictionary
            adj_pipes[(x,y)] = adjacent_pipes((x,y))

    # part 1
    path = get_path(adj_pipes, start_position)
    p1 = len(path) / 2

    # part 2
    # we now have the path of the pipes through the map. 
    # reset any junk pipes not in the path to be '.'
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            if (x,y) not in path:
                puzzle_input[y] = puzzle_input[y][:x] + '.' + puzzle_input[y][x+1:]

    # now scan each row, from l-r. A point is in the pipe loop if we have to traverse the loop an odd number of times.
    # traversing the pipe loop is stepping over any vertical piece of pipe, which is |
    # but L-7 and F-J should also be considered vertical (albeit staggered).

    for y in puzzle_input:
        # a nasty bit of hardcoding below. ToDo: Derive what S should be from the map
        y = y.replace('S', '|')

        for idx, x in enumerate(y):
            if x == '.':
                # if an odd number, we are inside the loop
                if len(re.findall('\||L-*7|F-*J', y[0:idx])) % 2 == 1:
                    p2+=1

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 10
puzzle_input = AoC.load_puzzle_input(day,False)
solve()
