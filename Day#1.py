with open("CodeAdvent2023/day1.txt") as file:
    data = [i for i in file.read().strip().split()]

# part1
part_one_solution = 0

for line in data:
    digits = [i for i in line if i.isdigit()]
    part_one_solution += int(digits[0]+digits[-1])

print(f"Part 1: {part_one_solution}")


# part2 # that one is not my idea, its @hyper-neutrino work
part_two_solution = 0

import re
spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pattern = "(?=(" + '|'.join(spelled_numbers) + "|\\d))"

def foo(x):
    if x in spelled_numbers:
        return str(spelled_numbers.index(x) + 1)
    return x

for line in data:
    digits = [*map(foo, re.findall(pattern, line))]
    part_two_solution += int(digits[0] + digits[-1])

print(f"Part 2: {part_two_solution}")