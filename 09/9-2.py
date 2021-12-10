from math import prod 

with open('input') as file:
    input = [[int(i) for i in line.strip()] for line in file]

shape = (len(input), len(input[0]))

def get_value(x, y):
    return input[x][y] if 0 <= x < shape[0] and 0 <= y < shape[1] else 9

def adjacent(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def explore_basin(basin, x, y):
    for x_a, y_a in adjacent(x, y):
        if input[x][y] <= get_value(x_a, y_a) != 9 and (x_a, y_a) not in basin:
            basin.add((x_a, y_a))
            explore_basin(basin, x_a, y_a)

basins = []
for x in range(shape[0]):
    for y in range(shape[1]):
        if input[x][y] != 9 and all(get_value(i[0], i[1]) > input[x][y] for i in adjacent(x, y)):
            basin = {(x, y)}
            basins.append(basin)
            explore_basin(basin, x, y)

basins.sort(key = len, reverse = True)
print([len(basin) for basin in basins[0:3]])
answer = prod(len(basin) for basin in basins[0:3])

print(f'Answer: {answer}')
