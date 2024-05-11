from collections import deque as dq

with open("CodeAdvent//CodeAdvent2023//day10.txt") as file:
    grid = [i for i in file.read().strip().splitlines()]

# finding main loop
around_poss = {
    (-1, 0): ["-J7", "-LF"],
    (1, 0): ["-LF", "-J7"],
    (0, 1): ["|7F", "|JL"],  # two last ones are inverted because
    (0, -1): ["|JL", "|7F"],  # axis Y grows downwward
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

# replacing 'S' with sth from '-|LFJ7'
rep = []
for x, y in around_poss:
    if ((SX + x, SY + y) in pipes) and (grid[SY + y][SX + x] in around_poss[(x, y)][1]):
        rep.append(set(around_poss[(x, y)][0]))
grid[SY] = grid[SY].replace("S", (rep[0] & rep[1]).pop())

# main code of part 2
empty = set()
closed = False

for rx, r in enumerate(grid):
    last_curve = False
    closed = False
    for cx, c in enumerate(r):
        pipe = c
        if (cx, rx) in pipes:
            if pipe == "|":
                closed = not closed
            elif last_curve:
                if pipe == "7" and last_curve == "L":
                    closed = not closed
                elif pipe == "J" and last_curve == "F":
                    closed = not closed
            if pipe in "FL7J":
                last_curve = pipe
        elif not closed:
            empty.add((cx, rx))


p2_solution = (len(grid) * len(grid[0])) - len(pipes | empty)
print(p2_solution)
