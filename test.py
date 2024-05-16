import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def count_neighbors(cell, grid):
    x, y, z = cell
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == 0 and j == 0 and k == 0:
                    continue
                count += grid[(x + i) % len(grid), (y + j) % len(grid[0]), (z + k) % len(grid[0][0])]
    return count

def game_of_life_3d(grid):
    new_grid = np.copy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(len(grid[0][0])):
                live_neighbors = count_neighbors((x, y, z), grid)
                if grid[x, y, z] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[x, y, z] = 0
                else:
                    if live_neighbors == 3:
                        new_grid[x, y, z] = 1
    return new_grid

def visualize(grid):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(len(grid[0][0])):
                if grid[x, y, z] == 1:
                    ax.scatter(x, y, z, c='b')
    plt.show()

# Initialize grid
grid = np.random.randint(0, 2, size=(10, 10, 10))

# Run game of life
for i in range(10):
    visualize(grid)
    grid = game_of_life_3d(grid)