import numpy as np

with open('input') as file:
    grid = np.genfromtxt(file, dtype = int, delimiter = 1)

flash_target = grid.shape[0]*grid.shape[1]
flash_target_met = False
flash_step = 0
while not flash_target_met:
    grid += 1
    flash_set = set()
    while flash := set(zip(*np.where(grid > 9))).difference(flash_set):
        for point in flash:
            grid[max(0, point[0]-1):point[0]+2, max(0, point[1]-1):point[1]+2] += 1
        flash_set.update(flash)
    for point in flash_set:
        grid[point[0], point[1]] = 0
    flash_step += 1
    flash_target_met = len(flash_set) == flash_target
        
print(f'Answer {flash_step}')
