import numpy as np

def step(grid):
    move_list = []
    for x, y in zip(*np.where(grid == '>')):
        if grid[x][(y+1)%grid.shape[1]] == '.':
            move_list.append((x,y))
    for x, y in move_list:
        grid[x][y] = '.'
        grid[x][(y+1)%grid.shape[1]] = '>'
    changed = bool(move_list)

    move_list.clear()
    for x, y in zip(*np.where(grid == 'v')):
        if grid[(x+1)%grid.shape[0]][y] == '.':
            move_list.append((x,y))
    for x, y in move_list:
        grid[x][y] = '.'
        grid[(x+1)%grid.shape[0]][y] = 'v'
    changed |= bool(move_list)

    return changed

def solve(grid):
    steps = 0
    while step(grid):
        steps += 1
    return steps + 1 # Because we also count the first time nothing moves

with open('input') as file:
    grid = np.genfromtxt(file, dtype = str, delimiter = 1)
print(f'Answer: {solve(grid)}')