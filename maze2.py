###################################
# Python solution to maze2 lesson
# Jeff Wong
# Python 3.8.6
# 10.20.2021
###################################


def wall_left():
    return True


def wall_right():
    return True


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze2 = [[1, 1, 1, 1, 101, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
         [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 101, 1]]

start = (9, 6)  # (4, 0), (0, 2), (6, 9)
end = (0, 2)  # (4, 0), (0, 2), (6, 9)
ROW = 21
COL = 21
x = 0
y = 0
steps = 1

while (x, y) != end:
    while True:
        reply = input("Can you take a step forward? Yes or No\n")
        if reply != "Yes" or reply != "No":
            print("Error! Make sure you only enter either Yes or No")
        else:
            maze[x][y] = steps
            y += 1
            steps += 1
            break

    if reply == "No":
        while True:
            reply = input("Will you be turning left or right? Left or Right\n")
            if reply != "Left" or reply != "Right":
                print("Error! Make sure you only enter either Left or Right")
            elif reply == "Left":
                if x - 1 < 0:
                    print("Error! Unable to turn left")
                else:
                    x -= 1
                    break
            else:
                if x + 1 > ROW:
                    print("Error! Unable to turn right")
                else:
                    x += 1
                    break

# for i in range(0, ROW):
#     for j in range(0, COL):
#         print(str(maze[i][j]), end=" ")
#
#     print("")
