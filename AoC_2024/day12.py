
from aoc import AoC
from collections import defaultdict

# Note: this code has been heavily refactored from the original version used to solve the puzzle.
#       original version was way to embarrasing to publish!

seen = []

def solve(input):
    p1, p2 = 0, 0

    neighbours = defaultdict(list)
    perimeters = {}

    for r in range(len(input)):
        for c in range(len(input[0])):

            # create a dictionary of adjacent plots.
            # at the same time capture the number of perimeter edges for each plot.
            # we need to do this, rather than just considering the perimeter of the region, since the
            # region could be like a donut.

            neighbours[(r, c)] = []
            perimeter = 0

            # look at the plots left, right, above and below the current plot.
            for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:

                if 0 <= nr < len(input) and 0 <= nc < len(input[0]):
                    if input[r][c] == input[nr][nc]:
                        # it's the same crop. Add to the neigbours
                        neighbours[(r, c)].append((nr, nc))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1

            perimeters[(r, c)] = perimeter

    def get_neighbours(plot):
        global seen

        if plot in seen:
            return []

        seen += [plot]
        ret = [plot]

        if plot in neighbours:
            for neigbour in neighbours[plot]:
                ret += get_neighbours(neigbour)

        return ret

    # the neigbours dictionary contains a unique list of the plots. 
    # get a region that includes this plot.
    # as we iterate the plots, if we happen to visit one that's already been used as part of a previous region, 
    # then the returned region in this case will be empty.

    for key in neighbours.keys():
        region = get_neighbours(key)

        if region:

            # Part one

            area = len(region)

            perimeter = 0
            for plot in region:
                perimeter += perimeters[plot]
            
            p1 += area * perimeter

            # Part two. 
            #
            # Calculate fences around each region. Some funky logic here.
            #
            # Look at each plot in the region. if it have 4 neighours, then it's surrounded and doesn't have any fences.
            # Conversely, if it has no neighbours, then it's a single plot region and must have 4 fences.
            #
            # Otherwise, need some extra consideration. What we will do is look for the end of each fence.
            # So, or a top or bottom fence, the far left plot. For a left or right fence, the far upper plot.
            # then, sum these up to get the total fences.
            #
            # eg:  for  --      we will find:    -
            #          |AA|                     |AA| 
            #          |AA|                      AA
            #           --                       -
            #
            # Also need to consider where the far let (or far top) perimeter is internal.


            fences = 0

            for plot in region:

                if len(neighbours[plot]) == 4:
                    # plot has no exposed sides
                    continue

                if len(neighbours[plot]) == 0:
                    # plot is exposed all round.
                    fences += 4
                    continue

                r, c = plot

                checks = [
                    ((r - 1, c), (r, c - 1), (r - 1, c - 1)),  # Top perimeter
                    ((r + 1, c), (r, c - 1), (r + 1, c - 1)),  # Bottom perimeter
                    ((r, c - 1), (r - 1, c), (r - 1, c - 1)),  # Left perimeter
                    ((r, c + 1), (r - 1, c), (r - 1, c + 1))]  # Right perimeter
    
                for edge, adj, diag in checks:
                    if edge not in region:
                        if adj not in region or diag in region:
                            fences += 1

            p2 += area * fences

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 12
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)
