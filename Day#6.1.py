with open("CodeAdvent2023/day6.txt") as file:
    times, distances = [[int(j) for j in i.split(':')[1].strip().split()] for i in file.read().strip().splitlines()]

# part1
p1_solution = 1

for indx, time in enumerate(times):
    score = 0
    for t in range(time):
        if distances[indx] < (time-t)*t:
            score += 1
    p1_solution *= score

print(p1_solution)
#print(times, distances)