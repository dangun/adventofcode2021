import numpy as np

STEPS_TARGET = 100 

with open('input') as file:
    grid = np.genfromtxt(file, dtype = int, delimiter = 1)

flash_count = 0
for i in range(0, STEPS_TARGET):
    grid += 1
    flash_set = set()
    while flash := set(zip(*np.where(grid > 9))).difference(flash_set):
        for point in flash:
            grid[max(0, point[0]-1):point[0]+2, max(0, point[1]-1):point[1]+2] += 1
            flash_count += 1
        flash_set.update(flash)
    for point in flash_set:
        grid[point[0], point[1]] = 0

print(f'Answer: {flash_count}')
