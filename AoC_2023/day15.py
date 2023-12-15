from aoc import AoC
import re

def hash(s):
    
    # Returns the hashed value for the passed in string.

    t = 0
    for c in s:
        t = ((t + ord(c)) * 17) % 256 
    return t
  
def solve(input):
    p1, p2 = 0, 0

    steps = input.replace('\n','').split(',')

    # Part 1

    p1 = sum([hash(s) for s in steps])    

    # Part 2

    # Initialise a list of 256 dictionaries. Use dictionaries to track lens placements.

    boxes = [{} for _ in range(256)]

    for step in steps:

        label, value = re.split('=|-', step)
        box_no = hash(label)

        if '=' in step:
            boxes[box_no][label] = int(value)
        else:
            if label in boxes[box_no].keys():
                boxes[box_no].pop(label)

    # Calculate the answer.

    for b_idx, box in enumerate(boxes):
        for k_idx, key in enumerate(box.keys()):
            p2 += (b_idx+1)*(k_idx+1)*(box[key])

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')

day = 15
#puzzle_input = AoC.load_puzzle_input(day, 'test_input', False)
puzzle_input = AoC.load_puzzle_input(day, split_lines=False)  
solve(puzzle_input)
