with open("CodeAdvent2023/day9.txt") as file:
    data = [list(map(int, i.split())) for i in file.read().strip().splitlines()]


# part1
p1_solution = 0

for history in data:
    lasts = []
    while not all([True if not i else False for i in history]): 
        # could've gone also with history[-1] != 0 || 
        # not sum(history), but those are not that accurate i think
        new = []
        for indx, num in enumerate(history[1:]):
            new.append(num - history[indx])
        lasts.append(history[-1])
        history = new

    p1_solution += sum(lasts)

print(p1_solution)
# 2043183816

""" 
(59, (5389030, 2171198, 829954, 296818, 97186, 28097, 6685, 1081, 5, -66, -22, -3))
(59, (5389030, 2171198, 829954, 296818, 97186, 28097, 6685, 1081, 5))
"""