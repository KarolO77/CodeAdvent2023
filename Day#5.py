import re
with open('CodeAdvent2023\\day5.txt') as file:
    data = file.read().split('map:')

# sorting the data
pattern = "[0-9]+"
sections = []
seeds = [int(i) for i in re.findall(pattern, data[0])]
sections = [[i for i in line.splitlines() if re.findall(pattern, i)] for line in data[1:]]

# part1
p1_solution = max(seeds)

for seed in seeds:
    for category in sections:
        for nums in category:
            drs, srs, rlen = [int(i) for i in nums.split()] #destination range start//source range start//range length
            if srs <= seed < srs + rlen:
                seed += drs - srs
                break

    if seed < p1_solution:
        p1_solution = seed

print(f"Part 1: {p1_solution}") #389056265