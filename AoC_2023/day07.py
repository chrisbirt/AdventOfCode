from aoc import AoC
import functools

def hand_type(a):

    # count up how many Jokers 
    #   
    global joker_mode
    j = a.count('J') if joker_mode else 0
    
    # get a list of how many time each card occurs in the hand
    matches = [a.count(i) for i in a]

    # five of a kind, four of a kind + joker, full house, with one set being jokers
    if (5 in matches) or (4 in matches and j in [1,4]) or (3 in matches and 2 in matches and j in [2,3]):
        return 1

    # four of a kind, three of a kind + joker, or three of a kind IS joker, + one other, two pairs where one pair is joker
    if (4 in matches) or (3 in matches and j in [1,3]) or (matches.count(2)==4 and j==2):
        return 2

    # full house, two pairs + joker
    if ((3 in matches) and (2 in matches)) or (matches.count(2)==4 and j==1):
        return 3

    # three of a kind, one pair + joker or pair is joker + one other
    if (3 in matches) or (matches.count(2)==2 and j in [1,2]):
        return 4

    # two pairs, 
    if matches.count(2) == 4:
        return 5
    
    # one pair, high card + joker
    if (matches.count(2) == 2) or (matches.count(1)==5 and j==1):
        return 6

    # high card
    if matches.count(1) == 5:
        return 7

def compare(a, b):

    global joker_mode

    hands = [a[0], b[0]]

    # Determine which types of hands we're comparing
    hand_types = [hand_type(hand) for hand in hands]

    # compare hand types
    if hand_types[0] < hand_types[1]:
        return 1
    elif hand_types[0] > hand_types[1]:
        return -1

    # If here, then hands are the same - compare the cards

    # first, create a dictionary to translate the cards to alpha-characters that can be string-compared.
    key_values = ['AKQT98765432J', 'abcdefghijklm'] if joker_mode else ['AKQJT98765432', 'abcdefghijklm']
    translate = dict(zip(key_values[0], key_values[1]))

    # map the hands to alphabetized strings
    hands = [[translate[i] for i in h] for h in hands]

    # compare cards in hands
    if hands[0] < hands[1]:
        return 1
    elif hands[0] > hands[1]:
        return -1
        
    return 0

def solve():
    global day, puzzle_input, joker_mode
    p1, p2 = 0, 0

    # format each row into a big list
    #
    # eg:  32T3K 765    becomes:  [['32T3K', 765], ['T55J5', 684]]
    #      T55J5 684
    #
    puzzle_input = [[j[0], int(j[1])] for j in [i.split(' ') for i in puzzle_input]]

    # sort the puzzle input 
    joker_mode = False
    puzzle_input = sorted(puzzle_input, key=functools.cmp_to_key(compare))

    # calculate the total winnings  
    p1 = sum([p[1]*(idx+1) for idx, p in enumerate(puzzle_input)])

    # part two - re-sort the puzzle input with jokers
    joker_mode = True
    puzzle_input = sorted(puzzle_input, key=functools.cmp_to_key(compare))

    # calculate the total winnings  
    p2 = sum([p[1]*(idx+1) for idx, p in enumerate(puzzle_input)])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

joker_mode = False
day = 7
puzzle_input = AoC.load_puzzle_input(day)
solve()
