import re
with open('CodeAdvent2023\\day5.txt') as file:
    data = file.read().split('map:')


# sorting the data
pattern = "[0-9]+"
seeds = [int(i) for i in re.findall(pattern, data[0])]
sections = [[i for i in line.splitlines() if re.findall(pattern, i)] for line in data[1:]]

sranges = [(i,i+seeds[2*indx+1]) for indx, i in enumerate(seeds[::2])]
ranges = set()
for start, end in sranges:
    ranges.update([*range(start,end)])


""" # part2
p2_solution = max(ranges)

for seed in ranges:
    for category in sections:
        for nums in category:
            drs, srs, rlen = [int(i) for i in nums.split()] #destination range start//source range start//range length
            if srs <= seed < srs + rlen:
                seed += drs - srs
                break

    if seed < p2_solution:
        p2_solution = seed

print(f"Part 2: {p2_solution}") """