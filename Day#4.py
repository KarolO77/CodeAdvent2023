with open("CodeAdvent2023\\day4.txt") as file:
    data = file.read().splitlines()


# part1
p1_solution = 0

for line in data:
    win_nums, equip = [i.split() for i in line.split(':')[1].split('|')]
    points = 0
    first = True
    for num in win_nums:
        if num in equip:
            if first:
                points += 1
                first = False
            else: points *= 2

    p1_solution += points
    
print(f'Part 1: {p1_solution}')


# part2
p2_solution = 0

copies = {i:1 for i in range(1, len(data)+1)}
for game, line in enumerate(data):
    win_nums, equip = [i.split() for i in line.split(':')[1].split('|')]
    num_of_wins = len([num for num in win_nums if num in equip])
    multiplier = copies[game+1] # all copies of game's card

    for indx in range(game+1, num_of_wins + game+1):
        copies[indx+1] += 1 * multiplier

p2_solution = sum(copies.values())
print(f'Part 2: {p2_solution}')