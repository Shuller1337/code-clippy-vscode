class Grid:
    def __init__(self, width, height):
        # Initialize the grid with the specified width and height
        self.width = width
        self.height = height
        # Create a 2D list to store particles, initially filled with None
        self.cells = [[None for _ in range(width)] for _ in range(height)]

    def update(self):
        # Update the grid by moving each particle
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x] is not None:
                    # Move each particle if it exists
                    self.cells[y][x].move(self)

    def display(self):
        # Display the grid
        for row in self.cells:
            # Print '.' for empty cells, or the particle type for occupied cells
            print(''.join(['.' if cell is None else cell.type for cell in row]))

class Particle:
    def __init__(self, x, y, particle_type):
        # Initialize a particle with position (x, y) and a type
        self.x = x
        self.y = y
        self.type = particle_type

    def move(self, grid):
        # Define the move method to be overridden by subclasses
        pass

    def interact(self, grid):
        # Define the interact method to be overridden by subclasses
        pass


class Sand(Particle):
    def __init__(self, x, y):
        # Initialize a sand particle with type 'S'
        super().__init__(x, y, 'S')

    def move(self, grid):
        # Move the sand particle down if the space below is empty
        if self.y + 1 < grid.height and grid.cells[self.y + 1][self.x] is None:
            # Move the particle down by updating the grid
            grid.cells[self.y][self.x] = None
            self.y += 1
            grid.cells[self.y][self.x] = self


class Water(Particle):
    def __init__(self, x, y):
        # Initialize a water particle with type 'W'
        super().__init__(x, y, 'W')

    def move(self, grid):
        # Move the water particle down, or to the sides if blocked
        if self.y + 1 < grid.height and grid.cells[self.y + 1][self.x] is None:
            # Move down
            grid.cells[self.y][self.x] = None
            self.y += 1
            grid.cells[self.y][self.x] = self
        elif self.x + 1 < grid.width and grid.cells[self.y][self.x + 1] is None:
            # Move right
            grid.cells[self.y][self.x] = None
            self.x += 1
            grid.cells[self.y][self.x] = self
        elif self.x - 1 >= 0 and grid.cells[self.y][self.x - 1] is None:
            # Move left
            grid.cells[self.y][self.x] = None
            self.x -= 1
            grid.cells[self.y][self.x] = self


def main():
    # Create a grid of size 10x10
    grid = Grid(10, 10)
    
    # Create sand and water particles
    sand1 = Sand(5, 0)
    water1 = Water(3, 0)
    
    # Place the particles in the grid
    grid.cells[sand1.y][sand1.x] = sand1
    grid.cells[water1.y][water1.x] = water1
    
    # Run the simulation for 10 steps
    for _ in range(10):
        # Update and display the grid
        grid.update()
        grid.display()
        print()  # Print a newline for better readability between steps

if __name__ == "__main__":
    main()
