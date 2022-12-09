def day2():

    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    
    map_part1 = {'A X': [3, 1], 'A Y': [6, 2], 'A Z': [0,3],
                 'B X': [0, 1], 'B Y': [3, 2], 'B Z': [6,3],
                 'C X': [6, 1], 'C Y': [0, 2], 'C Z': [3,3]}

    # A = Rock, B = Paper, C = Scissors
    # X = Lose, Y = Draw, Z = Win

    map_part2 = {'A X': [0, 3], 'A Y': [3, 1], 'A Z': [6,2],
                 'B X': [0, 1], 'B Y': [3, 2], 'B Z': [6,3],
                 'C X': [0, 2], 'C Y': [3, 3], 'C Z': [6,1]}
	
    with open('.\\input\\day2.txt', 'r') as f:
        # using splitlines removes the newline characters from the input
        puzzle_input = f.read().splitlines()

    results = [map_part1[x][0] + map_part1[x][1] for x in puzzle_input]
    print('Day 2, part 1:', sum(results))

    results = [map_part2[x][0] + map_part2[x][1] for x in puzzle_input]
    print('Day 2, part 2:', sum(results))


if __name__ == '__main__':
	day2()