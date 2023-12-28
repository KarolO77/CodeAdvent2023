with open("CodeAdvent2023/day8.txt") as file:
    data = [i for i in file.read().strip().splitlines()]
    nodes = {i[0:3] : (i[7:10], i[12:15]) for i in data[2:]}
    moves = data[0]

# part1
""" step = 0
node = 'AAA'
n = len(moves)
values = {'R' : 1, 'L' : 0}

while node != 'ZZZ':
    move = values[moves[step%n]]
    node = nodes[node][move]
    step += 1

print(f'Part 1: {step}') """


# part2
step = 0
n = len(moves)
values = {'R' : 1, 'L' : 0}
curr_nodes = [i for i in nodes.keys() if i[2] == 'A']
print(curr_nodes)

while True:
    move = values[moves[step%n]]
    step += 1

    curr_nodes = [nodes[node][move] for node in curr_nodes]

    if all([True if i[2] == 'Z' else False for i in curr_nodes]):
        break

print(f'Part 2: {step}')