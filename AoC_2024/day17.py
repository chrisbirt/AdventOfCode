from aoc import AoC
import re

def solve(input):
    p1, p2 = 0, 0
    reg_a, reg_b, reg_c = 0, 0, 0
    prog = []

    # parse the input

    for row in input:
        if 'A' in row:
            reg_a = int(row.split(' ')[-1])
        if 'B' in row:
            reg_b = int(row.split(' ')[-1])
        if 'C' in row:
            reg_c = int(row.split(' ')[-1])
        if 'Program' in row:
            prog = [int(r) for r in row.split(' ')[-1].split(',')]

    # refactored into a function for part two

    def run(a, b, c, p):

        ptr = 0
        ret = []

        while ptr < len(p):
            opcode, operand = p[ptr:ptr+2]

            # Combo operands 0 through 3 represent literal values 0 through 3.
            # Combo operand 4 represents the value of register A.
            # Combo operand 5 represents the value of register B.
            # Combo operand 6 represents the value of register C.
            # Combo operand 7 is reserved and will not appear in valid programs.

            if 0 <= operand <= 3:
                combo_operand = operand
            elif operand < 7:
                combo_operand = [a, b, c][operand-4]

            # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. 
            # The denominator is found by raising 2 to the power of the instruction's combo operand. 
            # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
            # The result of the division operation is truncated to an integer and then written to the A register."""

            if opcode == 0:
                a = int(a / (2 ** combo_operand))
                
            # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, 
            # then stores the result in register B.

            elif opcode == 1:
                b = b ^ operand

            # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), 
            # then writes that value to the B register.

            elif opcode == 2:
                b = combo_operand % 8

            # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, 
            # it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, 
            # the instruction pointer is not increased by 2 after this instruction.

            elif opcode == 3:
                if a != 0:
                    ptr = operand
                    continue

            # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. 
            # (For legacy reasons, this instruction reads an operand but ignores it.)

            elif opcode == 4:
                b = b ^ c

            # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. 
            # (If a program outputs multiple values, they are separated by commas.)

            elif opcode == 5:
                ret.append(combo_operand % 8)

            # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. 
            # (The numerator is still read from the A register.)

            elif opcode == 6:
                b = int(b / (2 ** combo_operand))

            # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. 
            # (The numerator is still read from the A register.)

            elif opcode == 7:
                c = int(a / (2 ** combo_operand))

            # Next instruction
            ptr += 2

        return ret

    p1 = ','.join(str(v) for v in run(reg_a, reg_b, reg_c, prog))

    # Part two.

    # By reverse-engineering the program, we can see the code executes as follows:
    #
    # Program       instruction             
    # 1: 2, 4       b = a % 8               
    # 2: 1, 5       b = b ^ 5               
    # 3: 7, 5       c = int(a / (2 ** b))   
    # 4: 4, 5       b = b ^ c               
    # 5: 0, 3       a = int(a / (2 ** 3))   <= THIS IS DECREMENTING A EACH LOOP
    # 6: 1, 6       b = b ^ 6               
    # 7: 5, 5       print(b % 8)            <= B IS ULTIMATELY A FUNCTION OF A. b = ((((a % 8) ^ 5) ^ (int(a / (2 ** ((a % 8) ^ 5))))) ^ 6) % 8
    # 8: 3, 0       if a != 0 goto 0        <= THIS CONTROLS LOOPING/ENDING
    #
    # My approach is to work back from the last value in the program, working out what values of reg_A will give the last value, 
    # then the last 2 values, then the last 3 values etc.
    
    # The key observation is that when int(reg_A / 2 ** 3)=0,  the program will have outputted a 0 (the last value in the program) and then ends.
    # So what value of reg_A will output a value of 0? It must be between 0 and 7 (since if reg_A > 7, the program won't end yet.)
    #
    # I find that when reg_A = 3, the program outputs 0.
    print(run(3, reg_b, reg_c, prog))

    # Next, what value of reg_A will produce int(reg_A / 2 ** 3)=3, and also output [3, 0]
    # reg_A must be a value between 24 and 31.
    #
    # I find that when reg_a = 24 or when reg_A = 31, we get an outut of [3, 0]
    print(run(24, reg_b, reg_c, prog))
    print(run(31, reg_b, reg_c, prog))

    # Then, what values of reg_a will produce int(reg_a / 2 ** 3)=24 or 31, and also output [5, 3, 0]
    # reg_A must be a value between 192 and 199 or between 248 and 255.
    #
    # I find that when reg_A = 192, 196, 198, 199 or 249, we get an output of [5, 3, 0]
    print(run(192, reg_b, reg_c, prog))
    print(run(196, reg_b, reg_c, prog))
    print(run(198, reg_b, reg_c, prog))
    print(run(199, reg_b, reg_c, prog))
    print(run(249, reg_b, reg_c, prog))

    # Generalising the approach, loop until the starting value of reg_A is found that produces an output that
    # matches the input

    seeds = [0]
    
    while True:
        new_seeds = []
        for s in seeds:
            for reg_a in range(s * 8, (s+1) * 8 ):
                output = run (reg_a, reg_b, reg_c, prog)
                # does the output match the end of the program?
                if output == prog[-len(output):]:
                    new_seeds.append(reg_a)
        seeds = new_seeds
            
        if len(output) == len(prog):
            break

    p2 = sorted(seeds)[0]

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


day = 17
puzzle_input = AoC.load_puzzle_input(day, False)
solve(puzzle_input)
