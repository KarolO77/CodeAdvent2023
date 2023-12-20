import re

with open("CodeAdvent2023/day2.txt") as file:
    data = [i for i in file.read().strip().split("\n")]


# part1
p1_solution = 0
game_pattern = r"Game [0-9]+: "
colors = {'red':12, 'green':13, 'blue':14}

def check_subset(subset):
    for i, c in subset: # integer, color
        if int(i) > colors[c]:
            return False
    return True

for indx, line in enumerate(data):
    line = [[bag.strip().split() for bag in subset.split(',')] for subset in 
            re.split(game_pattern, line)[1].split(';')]

    possible = True
    for subset in line:
        if not check_subset(subset):
            possible = False
            break

    if possible: p1_solution += indx+1

print(f'Part 1: {p1_solution}')


# part2
p2_solution = 0
game_pattern = r"Game [0-9]+: "

for line in data:
    line = [[bag.strip().split() for bag in subset.split(',')]
            for subset in 
            re.split(game_pattern, line)[1].split(';')]

    colors_max = {'red':0, 'green':0, 'blue':0}
    for subset in line:
        for i, c in subset: # integer, color
            if int(i) > colors_max[c]:
                colors_max[c] = int(i)

    r,g,b = colors_max.values()
    p2_solution += r*g*b

print(f'Part 2: {p2_solution}')