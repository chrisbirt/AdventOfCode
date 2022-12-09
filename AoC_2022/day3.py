def priority(item):
    # ascii reference: A=65, Z=90, a=97, z=122
    # priority: A=27, Z=52, a=1, z=26
    ord_item = ord(item)
    if (ord_item >= 65) & (ord_item <= 90):
        return ord_item - 38
    else:
        return ord_item - 96


def day3():

    with open('.\\input\\day3.txt', 'r') as f:
        # using splitlines removes the newline characters from the input
        puzzle_input = f.read().splitlines()

    result = 0
       
    for contents in puzzle_input:
        compartment1, compartment2 = contents[:len(contents) // 2], contents[len(contents) // 2:]
        common_item = [i for i in compartment1 if i in compartment2][0]
        result += priority(common_item)
           
    print('Day 3, part 1:', result)

    result = 0
    
    for i in range(0, len(puzzle_input), 3):
        rucksack1, rucksack2, rucksack3 = puzzle_input[i], puzzle_input[i+1], puzzle_input[i+2]
        common_item = [i for i in rucksack1 if (i in rucksack2) and (i in rucksack3)][0]
        result += priority(common_item)

    print('Day 3, part 2:', result)


if __name__ == '__main__':
	day3()