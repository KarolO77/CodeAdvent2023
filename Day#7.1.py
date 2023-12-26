from collections import Counter

with open("CodeAdvent2023/day7.txt") as file:
    data = [i.split() for i in file.read().strip().splitlines()]

Values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
Values.update({str(i):i for i in range(2,10)})

Types = {
    '5' : [],
    '41' : [],
    '32' : [],
    '311' : [],
    '221' : [],
    '2111' : [],
    '11111' : []
}

# part1
p1_solution = 0

# sorting
for line in data: # by number of pairs
    amount_of_pairs = sorted(Counter(line[0]).values(), reverse=True)
    key = "".join(map(str, amount_of_pairs))
    Types[key].append(line)

keys = list(Types.keys())
for typeIndx, Type in enumerate(Types.values()): # just sorting every rank
    if len(Type) > 1: # if set isnt empty
        # updated radixSort
        for i in range(1,6): # because 5 is a quantity of cards
            way = lambda x: Values[x[0][-i]]
            Type = sorted(Type, key=way)
    
        Types[keys[typeIndx]] = Type
    
c = 1
for Type in list(Types.values())[::-1]:
    for hand, bid in Type:
        p1_solution += int(bid) * c
        c += 1

print(p1_solution) 
# 251287184 LETS GOOOOO