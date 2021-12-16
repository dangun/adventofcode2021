import networkx as nx
import numpy as np

def neighbours (xy): 
    return [(xy[0] + 1, xy[1]), (xy[0], xy[1] + 1), (xy[0] - 1, xy[1]), (xy[0], xy[1] - 1)]

with open('input') as file:
    grid = np.genfromtxt(file, dtype = int, delimiter = 1)

G=nx.DiGraph()

it = np.nditer(grid, flags=['multi_index'])
for x in it:
    G.add_node((it.multi_index[0], it.multi_index[1]))
    for direction in neighbours((it.multi_index[0], it.multi_index[1])):
        if 0 <= direction[0] < grid.shape[0] and 0 <= direction[1] < grid.shape[1]:
            G.add_edge((it.multi_index[0], it.multi_index[1]), (direction[0], direction[1]), weight = grid[direction[0]][direction[1]])
    
path = nx.dijkstra_path(G, source=(0, 0), target=(grid.shape[0] - 1, grid.shape[1] - 1))
best = sum((grid[x][y] for x, y in path[1:]))

print(f'Answer: {best}')
