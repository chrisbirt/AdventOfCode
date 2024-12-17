from aoc import AoC
import re

## PARTIALLY COMPLETE

"""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

def solve(input):
    p1, p2 = [], 0
    reg_a, reg_b, reg_c = 0, 0, 0
    prog = []

    for row in input:
        if 'A' in row:
            reg_a = int(row.split(' ')[-1])
        if 'B' in row:
            reg_b = int(row.split(' ')[-1])
        if 'C' in row:
            reg_c = int(row.split(' ')[-1])
        if 'Program' in row:
            prog = [int(r) for r in row.split(' ')[-1].split(',')]

    print(reg_a, reg_b, reg_c, prog)


    def run(reg_a, reg_b, reg_c, prog):
        ptr = 0
        ret = []
        while ptr < len(prog):
            opcode, operand = prog[ptr:ptr+2]

            if 0 <= operand <= 3:
                combo_operand = operand
            elif operand < 7:
                combo_operand = [reg_a, reg_b, reg_c][operand-4]

    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. 
    # The denominator is found by raising 2 to the power of the instruction's combo operand. 
    # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
    # The result of the division operation is truncated to an integer and then written to the A register."""

            if opcode == 0:
                reg_a = int(reg_a / (2 ** combo_operand))
                
    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, 
    # then stores the result in register B.

            elif opcode == 1:
                reg_b = reg_b ^ operand

    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), 
    # then writes that value to the B register.

            elif opcode == 2:
                reg_b = combo_operand % 8

    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, 
    # it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, 
    # the instruction pointer is not increased by 2 after this instruction.

            elif opcode == 3:
                if reg_a != 0:
                    ptr = operand
                    continue

    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. 
    # (For legacy reasons, this instruction reads an operand but ignores it.)

            elif opcode == 4:
                reg_b = reg_b ^ reg_c

    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. 
    # (If a program outputs multiple values, they are separated by commas.)

            elif opcode == 5:
                ret.append(combo_operand % 8)
                if ret[-1] != prog[len(ret)-1]:
                    return []

    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. 
    # (The numerator is still read from the A register.)

            elif opcode == 6:
                reg_b = int(reg_a / (2 ** combo_operand))

    # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. 
    # (The numerator is still read from the A register.)

            elif opcode == 7:
                reg_c = int(reg_a / (2 ** combo_operand))

            ptr += 2

        return ','.join([str(r) for r in ret])


    p1 = run(reg_a, reg_b, reg_c, prog)

    # 4,6,3,5,6,3,5,2,1,0
    # 4,6,3,5,6,3,5,2,1,0

    prog_exp = ','.join([str(p) for p in prog])
    prog_act = ''

    reg_a = 0
    while prog_exp != prog_act:
        reg_a += 1
        prog_act = run(reg_a, reg_b, reg_c, prog)
        #print(reg_a, reg_b, reg_c, prog, prog_act)

    p2 = reg_a

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 17
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)
