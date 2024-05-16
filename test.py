import numpy as np
import vpython as vp

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
    vp.scene = vp.canvas(title="3D Game of Life", width=800, height=600)
    vp.rate(30)
    boxes = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(len(grid[0][0])):
                if grid[x, y, z] == 1:
                    boxes[(x, y, z)] = vp.box(pos=vp.vector(x, y, z), size=vp.vector(0.9, 0.9, 0.9), color=vp.color.red)
    while True:
        grid = game_of_life_3d(grid)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for z in range(len(grid[0][0])):
                    if grid[x, y, z] == 1 and (x, y, z) not in boxes:
                        boxes[(x, y, z)] = vp.box(pos=vp.vector(x, y, z), size=vp.vector(0.9, 0.9, 0.9), color=vp.color.red)
                    elif grid[x, y, z] == 0 and (x, y, z) in boxes:
                        boxes[(x, y, z)].visible = False
                        del boxes[(x, y, z)]
        vp.rate(30)

# Initialize grid
grid = np.random.randint(0, 2, size=(10, 10, 10))

# Run game of life
visualize(grid)