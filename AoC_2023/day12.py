from aoc import AoC
from itertools import combinations
import re

def find_matches(spring_map, groups, in_group=False):

    global cache
    
    # by default, assume we will return zero, unless a non-zero result is calculated
    ret = 0

    # if the spring map is empty, then no more can be done.
    #
    if not spring_map and not groups:
        return 1
    if not spring_map and sum(groups)==0:
        return 1
    if not spring_map and sum(groups)>0:
        return 0
    
    # construct a string key to cache the match count for this sequence
    #
    cache_key = str(spring_map) + str(groups) + str(in_group)

    # if it's in the cache, just return the value
    #
    if cache_key in cache:
        return cache[cache_key]

    # look at the first character in the string map
    #
    if spring_map[0] == '.':

        # if up to this point we've been processing a group, then we should now be stepping out of the group.
        # so, if the group value is now zero, then all is good, continue with the rest of the string, 
        # and remove that (now zero) group. Else, just return zero.
        #
        if in_group:
            if groups[0] == 0:
                ret = find_matches(spring_map[1:], groups[1:])

        # if we have not been processing a group, then just continue for the rest of the string
        #
        else:
            ret = find_matches(spring_map[1:], groups)

    # look at the first character in the string map
    #
    elif spring_map[0] == '#':

        # if up to this point we've NOT been processing a group, then we should enter 'in group' mode.
        #   if there are no groups left to process, or the first available group is zero, then return zero.
        #   else, decrement the first group by 1, and call for the rest of the string
        #
        if groups:
            if groups[0] > 0:
                groups[0] -= 1
                ret = find_matches(spring_map[1:], groups, True)

    # it's a wild card, so replace with both characters and try both paths
    #
    elif spring_map[0] == '?':
        
        for x in ['.', '#']:
            ret += find_matches(x + spring_map[1:], groups[:], in_group)

    # cache the result, and return
    #
    cache[cache_key] = ret
    return ret


def solve(input):
    p1, p2 = 0, 0

    for row in input:

        # part 1

        spring_map, groups = row.split(' ')
        groups = [int(i) for i in groups.split(',')]
        p1 += find_matches(spring_map, groups[:])

        # part 2

        spring_map = '?'.join([spring_map for i in range(5)])
        groups = groups * 5
        p2 += find_matches(spring_map, groups)

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


cache = {}
day = 12
#solve(AoC.load_puzzle_input(day, 'test_input'))
solve(AoC.load_puzzle_input(day))
