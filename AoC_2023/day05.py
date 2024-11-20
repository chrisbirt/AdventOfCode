from aoc import AoC

def solve(input):

    p1, p2 = 0, 0
    seeds, locations, map_set, all_map_sets = [], [], [], []

    for row in input:

        if 'seeds' in row:
            # eg: seeds: 82 1 79 14 55 13  becomes [82, 1, 79, 14, 55, 13]
            #
            seeds = [int(n) for n in row.split(' ')[1:]]

            # For part two: [82, 1, 79, 14, 55, 13] becomes [[82, 83], [79, 93], [55, 68]]
            #
            seed_ranges = [[seeds[x], seeds[x] + seeds[x+1] - 1] for x in range(0, len(seeds), 2)]

        elif 'map' in row:
            # We are entering set of mappings. 
            # For the first set, map_set will be empty. Otherwise, it'll contain the maps from the prior mapping. Store them.
            #
            if map_set:
                all_map_sets.append(map_set)
                map_set = []
        
        elif row != '':
            # Ignoring blank lines, anything not already handled above must be a mapping.
            # eg: 50 98 2  becomes  [-48, 98, 99] (offset, min, max)
            #
            r = [int(r) for r in row.split(' ')]
            map_set.append([r[0] - r[1], r[1], r[1] + r[2] - 1])
    
    # Store the last set of maps
    #
    all_map_sets.append(map_set)

    # Part one. For each seed value, run it through the mappings.
    #
    for s in seeds:
        for map_set in all_map_sets:
            # Find the first map in the map set for which s is in the range
            #
            s += next((m[0] for m in map_set if m[1] <= s <= m[2]), 0)

        # Store the mapped seed value.
        #
        locations += [s]

    p1 = min(locations)

    # Part two. The seeds are actually pairs of seed ranges.
    # For each map set, cycle round all the seed ranges. 
    # When a seed range overlaps the mapping range, work out what's NOT mapped, and add as a new mapping to be treated separately.
    #
    for map_set in all_map_sets:
        idx = 0

        while idx < len(seed_ranges):
            sr = seed_ranges[idx]

            for m in map_set:

                # If seed range overlaps the beginning of the mapping range,
                # split the range, adding a new range for the non-overlapping portion.
                #
                if (sr[0] < m[1]) & ((sr[1]) >= m[1]):
                    seed_ranges.append([sr[0], m[1] - 1])
                    sr[0] = m[1]

                # If seed range overlaps the end of the mapping range,
                # split the range, adding a new range for the non-overlapping portion.
                #
                if (sr[0] <= m[2]) & (sr[1] > m[2]):
                    seed_ranges.append([m[2] + 1, sr[1]])
                    sr[1] = m[2]
                
                # Finally, if the adjusted seed range is in the mapping range, then map it.
                if m[1] <= sr[0] <= sr[1] <= m[2]:
                    sr[0] += m[0]
                    sr[1] += m[0]
                    break

            idx += 1

    p2 = min([sr[0] for sr in seed_ranges])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 5
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)