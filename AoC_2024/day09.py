from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0

    # Expand dense format into a map
    # The map is a 2d list, with each point on the map containing the file_id (or -1 for a space), and then length of the file
    # (or in the case of a space, the number of remaining spaces to the right)
    #
    # eg : 23331
    # becomes:     [[0, 2], [0, 2], [-1, 3], [-1, 2], [-1, 1], [1, 3], [1, 3], [1, 3], [-1, 3], [-1, 2], [-1, 1], [2, 1]]

    start_map = []

    for i, val in enumerate(input):
        val = int(val)
        if i % 2 == 1:
            # Free space
            start_map += [(-1, val - j) for j in range(val)]
        else:
            # File
            start_map += [(i // 2, val) for j in range(val)]

    # Remove any trailing spaces.
    while start_map[-1][0] == -1: map.pop()

    # Part one.
    map = start_map[:]

    for i, m in enumerate(map):
        if m[0] == -1:
            # Found an empty space. Fill with a copy of the last file block.
            map[i]=map[-1]
            # Delete the file block.
            map.pop()
            # Purge any empty spaces at the end.
            while map[-1][0] == -1: map.pop()

    p1 = sum(i * j[0] for i, j in enumerate(map) if j[0] != -1)

    # Part two.
    map = start_map[:]

    # Find the id of the last file in the range.
    file_id = map[-1][0]

    # Get the index of the last file block.
    file_idx = len(map) - 1

    while file_idx >= 0:
        if map[file_idx][0] == file_id:
            file = map[file_idx]
            for space_idx in range(file_idx):
                #Find a space that's big enough.
                if map[space_idx][0] == -1 and map[space_idx][1] >= map[file_idx][1]:
                    map[space_idx : space_idx + file[1]] = map[file_idx - file[1] + 1 : file_idx + 1]
                    map[file_idx - file[1] + 1 : file_idx + 1] = [ [-1, 0] ] * file[1]
                    break
            file_idx -= file[1]
            file_id -= 1
        else:
            file_idx -= 1

    p2 = sum(i * j[0] for i, j in enumerate(map) if j[0] != -1)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 9
puzzle_input = AoC.load_puzzle_input(day, True, split_lines=False)
solve(puzzle_input)
