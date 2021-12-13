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

for instruction in instructions[:1]:
    fold_line = instruction[1]
    flip_set = set(dot for dot in dots if dot[flip_line[instruction[0]]] > fold_line )
    for dot in flip_set:
        dots.add(flip_method[instruction[0]](dot))
    dots = (dots - flip_set)

print(f'Answer: {len(dots)}')
