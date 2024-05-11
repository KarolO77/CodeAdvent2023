with open("CodeAdvent\\CodeAdvent2023\\day5.txt") as file:
    data = file.read().split("\n\n")


# sorting the data
seeds = [int(i) for i in data[0].split()[1:]]
stages = [
    [[int(i) for i in l.split()] for l in line.splitlines()[1:]] for line in data[1:]
]
""" seeds = {seed
    for indx, i in enumerate(seeds[::2])
    for seed in range(i,i+seeds[2*indx+1])
    } """
seeds = [(i, i + seeds[2 * indx + 1]) for indx, i in enumerate(seeds[::2])]

for way in stages:
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for drs, srs, rlen in way:
            ostart = max(start, srs)
            oend = min(end, srs + rlen)
            if ostart < oend:
                new.append((ostart + drs - srs, oend + drs - srs))
                if ostart > start:
                    seeds.append((start, ostart))
                if end > oend:
                    seeds.append((oend, end))
                break
        else:
            new.append((ostart, oend))
    seeds = new

p2_solution = min(seeds)
print(f"Part 2: {p2_solution[0]}")
