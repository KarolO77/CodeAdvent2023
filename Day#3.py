import re
with open("CodeAdvent2023/day3.txt") as file:
    data = [i for i in file.read().strip().splitlines()]



# part1
p1_solution = 0
nsymbol = '0987654321.'
pos_around = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def check_around(coordinates):
    for cindex in coordinates:
        for x,y in pos_around:
            try:
                if data[rindex+x][cindex+y] not in nsymbol:
                    return True
            except IndexError: continue

for rindex, row in enumerate(data):
    # get all numbers from row with their positions
    numbers = re.findall(r"\d+", row)
    num_indexs = []
    for i in numbers:
        indx = row.find(i)
        num_indexs.append([*range(indx, indx+len(i))])

    # for every number's positions check around it
    for num, coordinates in enumerate(num_indexs):
        if check_around(coordinates):
            p1_solution += int(numbers[num])

print(p1_solution)
#too low