import numpy as np
from operator import add

grid = np.zeros((101,101,101))
onoff = []
with open('input') as file:
    for line in file:
        op, coords = line.split(' ')
        xyz = [tuple(map(add, map(int, coord[2:].split('..')), (50,50,50))) for coord in coords.split(',')]
        if all(0 <= coord[0] <= 100 and 0 <= coord[1] <= 100 for coord in xyz):
            onoff.append((op, xyz))
for op, xyz in onoff:
    grid[xyz[0][0]:xyz[0][1]+1, xyz[1][0]:xyz[1][1]+1, xyz[2][0]:xyz[2][1]+1] = 1 if op == 'on' else 0

print(f'Answer: {np.count_nonzero(grid)}')