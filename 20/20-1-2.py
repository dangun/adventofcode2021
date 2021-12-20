import numpy as np

STEPS = 50

def parse_input(filename):
    with open(filename) as file:
        data = file.read().replace('#', '1').replace('.', '0').splitlines()
    algo = data[0]
    grid = np.genfromtxt(data[1:], dtype=str, delimiter = 1)
    return algo, grid

def step(grid):
    new_grid = np.empty_like(grid)
    it = np.nditer(grid, flags=['multi_index'])
    for _ in it:
        x, y = it.multi_index
        if 0 < x < grid.shape[0]-1 and 0 < y < grid.shape[1]-1:
            adj_grid = grid[x-1:x+2,y-1:y+2]
            algo_bin = ''.join((num for row in adj_grid for num in row ))
            new_grid[x][y] = algo[int(algo_bin,2)]
    return new_grid

def solve(grid):
    flip1 = '0'
    flip2 = algo[0]
    curr = flip1
    grid = np.pad(grid, 2, constant_values = (flip1))
    for _ in range(STEPS):
        grid = step(grid)
        curr = flip1 if curr == flip2 else flip2
        grid[:,[0,-1]] = grid[[0,-1]] = curr
        grid = np.pad(grid, 1, constant_values = (curr))
    return grid[1:grid.shape[0]-1, 1:grid.shape[1]-1]

algo, grid = parse_input('input')
grid = solve(grid)
answer = np.count_nonzero(grid == '1')
print(f'Answer: {answer}')
