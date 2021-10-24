from time import sleep


# # The screen clear function
# def screen_clear():
#     # # for mac and linux(here, os.name is 'posix')
#     # if os.name == 'posix':
#     #     _ = os.system('clear')
#     # else:
#     #     # for windows platfrom
#     #     _ = os.system('cls')
#     print("\033c")


class Maze:
    # maze can be replaced by the maze array generated by maze_array_generator.py

    maze = [['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '0', '0', '0', '1', '0', '0', '1', '0', '1'],
            ['1', '0', '1', '0', '1', '0', '1', '1', '0', '1'],
            ['1', '1', '1', '0', '1', '0', '0', '0', '0', '1'],
            ['1', '1', '1', '0', '1', '0', '1', '1', '1', '1'],
            ['1', '0', '0', '0', '0', '0', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '0', '1', '0', '0', '0', '1'],
            ['1', '0', '0', '0', '0', '1', '1', '1', '0', '1'],
            ['1', '0', '1', '0', '1', '1', '0', '0', '0', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1']]

    x = -1
    y = -1

    # 0 = "Up", 1 = "Left", 2 = "Down", 3 = "Right"
    facing = 0
    steps = []
    row = len(maze)
    col = len(maze[0])
    minimal_steps = []

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
        # print("   ", end="")
        # for i in range(0, self.row):
        # print("%2d" % i, end=" ")

        # print("")

        for i in range(0, self.row):
            # print("%2d" % i, end=" ")
            for j in range(0, self.col):
                if self.maze[i][j] == '1':
                    print("%2c" % '#', end=" ")
                else:
                    print("%2c" % '.', end=" ")
            print("")

    def print_steps(self):
        for step in self.steps:
            for i in range(0, self.row):
                for j in range(0, self.col):
                    if self.maze[i][j] == '1':
                        print("%c" % '#', end=" ")
                    elif (i, j) == step:
                        print("%s" % '\033[93m@\033[0m', end=" ")
                    else:
                        print("%c" % '.', end=" ")
                print("")

            sleep(0.3)
            print("\n" * 10)

    def print_minimal_steps(self):
        for i, step in enumerate(self.minimal_steps):
            print("%d: " % i + str(step))

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

    def at_exit(self):
        return (self.x, self.y) == (self.end_x, self.end_y)

    def minimal_path(self):
        visited = [[0 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]
        previous = [[-1 for x in range(len(self.maze[0]))] for y in range(len(self.maze))]

        queue = [(self.start_x, self.start_y)]

        while len(queue) != 0:
            x, y = queue.pop(0)

            if (x, y) == (self.end_x, self.end_y):
                break

            for directions in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                next_x, next_y = directions[0], directions[1]

                if 0 <= next_x < self.row and 0 <= next_y < self.col and self.maze[next_x][next_y] != '1':
                    if visited[next_x][next_y] == 0:
                        visited[next_x][next_y] = 1
                        previous[next_x][next_y] = x * self.row + y
                        queue.append((next_x, next_y))

        self.minimal_steps = []

        x, y = self.end_x, self.end_y
        while previous[x][y] != self.start_x * self.row + self.start_y:
            self.minimal_steps.insert(0, (x, y))
            x = int(previous[x][y] / self.col)
            y = previous[x][y] % self.col


def main():
    """
    List of functions available for use and their definition:
            - step_forward()
            - turn_left()
            - turn_right()
            - check_left_wall()
            - check_right_wall()
            - check_front_wall()
            - at_exit()
    """

    # Students will be implementing the steps below this line

    # Solution 1: Right Hand Rule
    right_maze = Maze()

    while not right_maze.at_exit():
        if not right_maze.check_right_wall():
            right_maze.turn_right()
        while right_maze.check_front_wall():
            right_maze.turn_left()
        right_maze.step_forward()

    # right_maze.print_maze()
    right_maze.print_steps()

    # Solution 2: Left Hand Rule
    # left_maze = Maze()
    #
    # while not left_maze.at_exit():
    #     if not left_maze.check_left_wall():
    #         left_maze.turn_left()
    #     while left_maze.check_front_wall():
    #         left_maze.turn_right()
    #     left_maze.step_forward()
    #
    # left_maze.print_steps()
    # left_maze.print_maze()

    # left_maze.minimal_path()
    # left_maze.print_minimal_steps()

    return 0


if __name__ == "__main__":
    main()
