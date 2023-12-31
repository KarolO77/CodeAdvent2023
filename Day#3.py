with open("CodeAdvent2023/day3.txt") as file:
    data = [i for i in file.read().strip().splitlines()]

# part1
p1_solution = 0
posistions = set()
pos_around = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def check_around():
    for x,y in pos_around:
        x = cindex+x
        y = rindex+y
        l = 1
        if data[y][x].isdigit() and 0 <= x < len(row) and 0 <= y < len(data):
            while data[y][x-l].isdigit() and x-l >= 0 and x-l <= len(row):
                    l += 1
            posistions.add((x-l+1,y))

for rindex, row in enumerate(data):
    for cindex, symbol in enumerate(row):
        if symbol not in '0987654321.':
            check_around()

for x, y in posistions:
    num = ''
    while x < len(row) and data[y][x].isdigit():
        num += data[y][x]
        x += 1
    p1_solution += int(num)

print(p1_solution) 
#521242
#too low
#523129
#1087402
#849081
#1087402
#521601