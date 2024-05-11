with open("CodeAdvent//CodeAdvent2023//day11.txt") as file:
    grid = file.read().splitlines()

empty_rows = []
empty_cols = []

# rows
row_end = len(grid[0])
for rx, row in enumerate(grid):
    for cx, col in enumerate(row):
        if col == "#":
            cx -= 1
            break
    if cx + 1 == row_end:
        empty_rows.append(rx)

# columns
col_end = len(grid)
for i in range(row_end):
    for rx, row in enumerate(grid):
        if row[i] == "#":
            rx -= 1
            break
    if rx + 1 == col_end:
        empty_cols.append(i)

# inserting
for k, rx in enumerate(empty_rows):
    grid.insert(rx + k, row_end * ".")

for k, col in enumerate(empty_cols):
    for rx, row in enumerate(grid):
        grid[rx] = row[: col + k] + "." + row[col + k :]

# galaxies
galaxies = []
total = 0

for rx, row in enumerate(grid):
    for cx, col in enumerate(row):
        if col == "#":
            galaxies.append((cx, rx))

for gal_indx, g in enumerate(galaxies):
    for dx, dy in galaxies[gal_indx + 1 :]:
        total += abs(g[0] - dx) + abs(g[1] - dy)

print(total)
