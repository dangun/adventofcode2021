depth = 0
horiz = 0
aim = 0

movements = [(line[0], int(line[1])) for line in map(str.split, open('input'))]

for move in movements:
    match move[0]:
        case 'forward':
            horiz += move[1]
            depth += aim * move[1]
        case 'down':
            aim += move[1]
        case 'up':
            aim -= move[1]

print(depth*horiz)