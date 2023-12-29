with open("CodeAdvent2023/day8.txt") as file:
    data = [i for i in file.read().strip().splitlines()]
    nodes = {i[0:3] : (i[7:10], i[12:15]) for i in data[2:]}
    moves = data[0]

# part1
step = 0
node = 'AAA'
n = len(moves)
values = {'R' : 1, 'L' : 0}

while node != 'ZZZ':
    move = values[moves[step%n]]
    node = nodes[node][move]
    step += 1

print(f'Part 1: {step}')