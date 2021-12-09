with open('input') as file:
    input = [[int(i) for i in line.strip()] for line in file]

shape = (len(input), len(input[0]))

def get_value(x, y):
    return input[x][y] if 0 <= x < shape[0] and 0 <= y < shape[1] else 9

def adjacent(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

risk_level = 0
for x in range(shape[0]):
    for y in range(shape[1]):
        if input[x][y] != 9 and all(get_value(i[0], i[1]) > input[x][y] for i in adjacent(x, y)):
            risk_level += input[x][y] + 1

print(f'Answer: {risk_level}')
