from aoc import AoC
from itertools import product
import re

def solve(input):
    p1, p2 = 0, 0

    # '190: 10 19' becomes ['190', '10', '19']
    input = [[int(row[0])] + row[1:] for row in (re.split(': | ', row) for row in input)]

    def is_valid(row, operands):
        result = row[0]
        numbers = row[1:]

        # pre-calc operand combinations. All combinations of length one less than the number of numbers
        ocs = [o for o in list(product(operands, repeat=len(numbers)-1)) if len(o) == (len(numbers)-1)]

        for oc in ocs:
            total = int(numbers[0])
            for i, operand in enumerate(oc):
                if operand == '|':
                    total = int(str(total) + numbers[i + 1])
                else:
                    total = eval(str(total) + operand + numbers[i + 1])
            if total == result:
                return True
        return False

    p1 = sum(row[0] for row in input if is_valid(row, ['+', '*']))
    p2 = sum(row[0] for row in input if is_valid(row, ['+', '*', '|']))

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 7
puzzle_input = AoC.load_puzzle_input(day)
solve(puzzle_input)

# solve here
#2941973819040
#249943041417600

