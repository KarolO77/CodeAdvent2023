with open("CodeAdvent2023/day6.txt") as file:
    time, distance = [int("".join(i.split(':')[1].strip().split())) for i in file.read().strip().splitlines()]

# part2
for t in range(time):
    result = (time-t)*t
    if distance < (time-t)*t:
        p2_solution = time - 2*t + 1
        break

print(p2_solution)