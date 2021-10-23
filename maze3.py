class Maze:
    maze = [['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1'],
            ['1', '0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1'],
            ['1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '1'],
            ['1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1'],
            ['1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
            ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1'],
            ['1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '1'],
            ['1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1'],
            ['1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1'],
            ['1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
            ['1', '1', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
            ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1'],
            ['1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '1'],
            ['1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
            ['1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1'],
            ['1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
            ['1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1'],
            ['1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1']]

    x = -1
    y = -1

    # 0 = "Up", 1 = "Left", 2 = "Down", 3 = "Right"
    facing = 0
    steps = []
    row = 21
    col = 21

    def __init__(self):
        self.start_x, self.start_y = self.find_start(self.row, self.col)
        self.end_x, self.end_y = self.find_exit(self.col)
        self.x = self.start_x
        self.y = self.start_y
        self.steps.append((self.x, self.y))

    def find_start(self, row, col):
        start_y = -1
        for i in range(0, col):
            if self.maze[row - 1][i] == "0":
                start_y = i
        if start_y == -1:
            print("Error: Could not find starting point.")
            return -1
        else:
            return row - 1, start_y

    def find_exit(self, col):
        end_y = -1
        for i in range(0, col):
            if self.maze[0][i] == "0":
                end_y = i
        if end_y == -1:
            print("Error: Could not find exit point.")
            return -1
        else:
            return 0, end_y

    def print_maze(self):
        print("   ", end="")
        for i in range(0, self.row):
            print("%2d" % i, end=" ")

        print("")

        for i in range(0, self.row):
            print("%2d" % i, end=" ")
            for j in range(0, self.col):
                print("%2c" % self.maze[i][j], end=" ")
            print("")

    def print_steps(self):
        for step in self.steps:
            print(step)

    def step_forward(self):
        allow = False

        # Facing Up
        if self.facing == 0:
            if self.maze[self.x - 1][self.y] != "1":
                self.x -= 1
                allow = True
        # Facing Left
        elif self.facing == 1:
            if self.maze[self.x][self.y - 1] != "1":
                self.y -= 1
                allow = True
        # Facing Down
        elif self.facing == 2:
            if self.maze[self.x + 1][self.y] != "1":
                self.x += 1
                allow = True
        # Facing Right
        elif self.facing == 3:
            if self.maze[self.x][self.y + 1] != "1":
                self.y += 1
                allow = True
        else:
            print("Error: Walking into a wall!")

        if not allow:
            print("Error: Walking into a wall!")
        else:
            self.steps.append((self.x, self.y))

        return allow

    def turn_left(self):
        self.facing = (self.facing + 1) % 4

    def turn_right(self):
        if self.facing == 0:
            self.facing = 3
        else:
            self.facing -= 1

    def check_left_wall(self):
        wall = False

        # Facing Up
        if self.facing == 0:
            if self.maze[self.x][self.y - 1] == "1":
                wall = True
        # Facing Left
        elif self.facing == 1:
            if self.maze[self.x + 1][self.y] == "1":
                wall = True
        # Facing Down
        elif self.facing == 2:
            if self.maze[self.x][self.y + 1] == "1":
                wall = True
        # Facing Right
        else:
            if self.maze[self.x - 1][self.y] == "1":
                wall = True

        return wall

    def check_right_wall(self):
        wall = False

        # Facing Up
        if self.facing == 0:
            if self.maze[self.x][self.y + 1] == "1":
                wall = True
        # Facing Left
        elif self.facing == 1:
            if self.maze[self.x - 1][self.y] == "1":
                wall = True
        # Facing Down
        elif self.facing == 2:
            if self.maze[self.x][self.y - 1] == "1":
                wall = True
        # Facing Right
        else:
            if self.maze[self.x + 1][self.y] == "1":
                wall = True

        return wall

    def check_front_wall(self):
        wall = False

        # Facing Up
        if self.facing == 0:
            if self.maze[self.x - 1][self.y] == "1":
                wall = True
        # Facing Left
        elif self.facing == 1:
            if self.maze[self.x][self.y - 1] == "1":
                wall = True
        # Facing Down
        elif self.facing == 2:
            if self.maze[self.x + 1][self.y] == "1":
                wall = True
        # Facing Right
        else:
            if self.maze[self.x][self.y + 1] == "1":
                wall = True

        return wall


def main():
    """
    List of functions to use and their definition:
            - step_forward()
            - turn_left()
            - turn_right()
            - check_left_wall()
            - check_right_wall()
            - check_front_wall()
    """

    maze = Maze()

    # Right Hand Rule
    while (maze.x, maze.y) != (maze.end_x, maze.end_y):
        if not maze.check_right_wall():
            maze.turn_right()
        while maze.check_front_wall():
            maze.turn_left()
        maze.step_forward()

    maze.print_steps()
    maze.print_maze()

    # Left Hand Rule
    left_maze = Maze()

    while (left_maze.x, left_maze.y) != (left_maze.end_x, left_maze.end_y):
        if not left_maze.check_left_wall():
            left_maze.turn_left()
        while left_maze.check_front_wall():
            left_maze.turn_right()
        left_maze.step_forward()

    left_maze.print_steps()
    left_maze.print_maze()

    return 0


if __name__ == "__main__":
    main()
