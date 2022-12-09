def day1():

    with open('.\\input\\day1.txt', 'r') as f:
        # using splitlines removes the newline characters from the input
        puzzle_input = f.read().splitlines()
        
    elves_calories = []
    sum_calories = 0
    
    for calories in puzzle_input:
        if calories == '': 
            elves_calories.append(sum_calories)
            sum_calories = 0
        else:
            sum_calories += int(calories)

    print('Day 1, part 1:', max(elves_calories))
    
    elves_calories.sort()
    print('Day 1, part 2:', sum(elves_calories[-3:]))


if __name__ == '__main__':
    day1()
