with open("CodeAdvent2023/day9.txt") as file:
    data = [list(map(int, i.split())) for i in file.read().strip().splitlines()]

# part2
p2_solution = 0

for history in data:
    starts = []
    while not all([True if not i else False for i in history]):
        new = []
        for indx, num in enumerate(history[1:]):
            new.append(num - history[indx])
        starts.append(history[0])
        history = new

    res = 0
    for i in starts[::-1]:
        res = i - res

    p2_solution += res
    
    
print(p2_solution)

""" 
5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0 
"""