from collections import deque as dq

with open("CodeAdvent//CodeAdvent2023/day10.txt") as file:
    grid = [i for i in file.read().strip().splitlines()]


# part1
p1_solution = 0

around_poss = {
    (-1, 0): ["-J7", "-LF"],
    (1, 0): ["-LF", "-J7"],
    (0, 1): ["|7F", "|JL"],  # in list y-axis is 'inverted' and
    (0, -1): ["|JL", "|7F"],  # thats why i replaced these pipes
}
SX, SY = [(y.find("S"), indx) for indx, y in enumerate(grid) if y.find("S") != -1][0]
curr_poss = dq([(SX, SY)])
seen_pipes = {(SX, SY)}  # pipes through which I went

# DRAWING GRID, borders
right, bottom = len(grid[0]), len(grid)
sketch = [[" " for j in range(right)] for i in range(bottom)]
#sketch[SY][SX] = "S"

while curr_poss:
    cx, cy = curr_poss.popleft()
    curr_pipe = grid[cy][cx]

    for x, y in around_poss:
        new_pos = (cx + x, cy + y)
        cc, nc = around_poss[(x, y)]

        # DRAWING GRID
        sketch[cy][cx] = curr_pipe

        if 0 <= cy + y < len(grid) and 0 <= cx + x < len(grid[0]):
            if (
                (curr_pipe in cc + "S")
                and (grid[cy + y][cx + x] in nc)
                and (new_pos not in seen_pipes)
            ):
                seen_pipes.add(new_pos)
                curr_poss.append(new_pos)

    # DRAWING history of GRID
    """ for row in sketch:
        print("".join(row)) """



# 6282
p1_solution = len(seen_pipes) // 2
print(p1_solution)

# DRAWING GRID
for row in sketch:
    print("".join(row))

print(SX,SY)