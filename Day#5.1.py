with open("CodeAdvent\\CodeAdvent2023\\day5.txt") as file:
    data = file.read().split("\n\n")

# sorting the data
seeds = [int(i) for i in data[0].split()[1:]]
stages = [
    [[int(i) for i in l.split()] for l in line.splitlines()[1:]] for line in data[1:]
]

# part1
p1_solution = max(seeds)


for way in stages:
    new = []
    for seed in seeds:
        for drs, srs, rlen in way:
            # destination range start//source range start//range length
            if srs <= seed < srs + rlen:  # if seed is in range
                new.append(seed + drs - srs)
                break
        else:
            new.append(seed)

    seeds = new

p1_solution = min(seeds)
print(f"Part 1: {p1_solution}")  # 389056265
