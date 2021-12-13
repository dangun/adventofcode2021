instructions = []
dots = set()

with open('input') as file:
    input = file.read().split('\n\n')
    for line in input[1].splitlines():
        axis, value = line.split()[-1].strip().split('=')
        instructions.append((axis, int(value)))
    for line in input[0].splitlines():
        dots.add(tuple(map(int,line.strip().split(','))))

flip_x = lambda xy: ((2 * fold_line) - xy[0], xy[1])
flip_y = lambda xy: (xy[0], (2 * fold_line) - xy[1])

flip_method = {'x': flip_x, 'y': flip_y}
flip_line = {'x': 0, 'y': 1}

for instruction in instructions:
    fold_line = instruction[1]
    flip_set = set(dot for dot in dots if dot[flip_line[instruction[0]]] > fold_line )
    for dot in flip_set:
        dots.add(flip_method[instruction[0]](dot))
    dots = (dots - flip_set)

max_y = next(instr[1] for instr in instructions[::-1] if instr[0] == 'y')
max_x = next(instr[1] for instr in instructions[::-1] if instr[0] == 'x')

grid = [[' ']*max_x for _ in range(max_y)]

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

print('Answer:')
for line in grid:
    print(''.join(line))
