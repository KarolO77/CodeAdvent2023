from collections import deque as dq

with open("CodeAdvent//CodeAdvent2023//day10.txt") as file:
    grid = [i for i in file.read().strip().splitlines()]

# part2
around_poss = {
    (-1, 0): ["-J7", "-LF"],
    (1, 0): ["-LF", "-J7"],
    (0, 1): ["|7F", "|JL"], # two last ones are inverted because
    (0, -1): ["|JL", "|7F"], # axis Y grows downwward
}
SX, SY = [(y.find("S"), indx) for indx, y in enumerate(grid) if y.find("S") != -1][0]
curr_poss = dq([(SX, SY)])
pipes = {(SX, SY)}

while curr_poss:
    cx, cy = curr_poss.popleft()
    curr_pipe = grid[cy][cx]

    for x, y in around_poss:
        new_pos = (cx + x, cy + y)
        cc, nc = around_poss[(x, y)]

        if 0 <= cy + y < len(grid) and 0 <= cx + x < len(grid[0]):
            if (
                (curr_pipe in cc + "S")
                and (grid[cy + y][cx + x] in nc)
                and (new_pos not in pipes)
            ):
                pipes.add(new_pos)
                curr_poss.append(new_pos)

#grid[SY] = grid[SY][:SX]+'J'+grid[SY][SX+1:]

new_s = []
for x,y in around_poss:
    if ((SX+x,SY+y) in pipes) and (grid[SY+y][SX+x] in around_poss[(x,y)][1]):
        new_s.append(set(around_poss[(x,y)][0]))
print(new_s[0] & new_s[1])