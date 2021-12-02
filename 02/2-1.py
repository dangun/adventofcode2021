depth = 0
horiz = 0

movements = [(line[0], int(line[1])) for line in map(str.split, open('input'))]
    
for move in movements:
    match move[0]:
        case 'forward':
            horiz += move[1]
        case 'down':
            depth += move[1]
        case 'up':
            depth -= move[1]

print(depth*horiz)