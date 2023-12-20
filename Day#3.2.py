with open("CodeAdvent2023/day3.txt") as file:
    data = [i for i in file.read().strip().splitlines()]

# part2
p2_solution = 0
posistions = []
pos_around = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def check_around():
    nums = set()
    for x,y in pos_around:
        x = cindex+x
        y = rindex+y
        l = 1
        if data[y][x].isdigit() and 0 <= x < len(row) and 0 <= y < len(data):
            while data[y][x-l].isdigit() and x-l >= 0 and x-l <= len(row):
                    l += 1
            nums.add((x-l+1,y)) # appends start pos of number that is attached to'*'

    if len(nums) == 2:
        posistions.append(nums)


for rindex, row in enumerate(data):
    for cindex, symbol in enumerate(row):
        if symbol == '*':
            check_around()


for a,b in posistions:
    nums = []
    for x,y in [a,b]:
        num = ''
        while x < len(row) and data[y][x].isdigit():
            num += data[y][x]
            x += 1
        nums.append(int(num))

    p2_solution += nums[0] * nums[1]
    

print(p2_solution)
#28573676 too low
#80694070