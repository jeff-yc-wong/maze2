###################################
# Python solution to maze2 lesson
# Jeff Wong
# Python 3.8.6
# 10.20.2021
###################################


maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

ROW = 10
COL = 10

steps = 1
directions = ["North", "East", "South", "West"]

# Ask for starting position
while True:
    reply = input("What row is the entrance in? 0-9\n")
    if not reply.isnumeric():
        print("Error! Make sure you enter only an integer")
    elif int(reply) < 0 or int(reply) > 9:
        print("Error! Make sure you only enter a value between 0 and 9 inclusive")
    else:
        start_x = int(reply)
        break

while True:
    reply = input("What column is the entrance in? 0-9\n")
    if not reply.isnumeric():
        print("Error! Make sure you enter only an integer")
    elif int(reply) < 0 or int(reply) > 9:
        print("Error! Make sure you only enter a value between 0 and 9 inclusive")
    else:
        start_y = int(reply)
        break

# Marking starting step on 10 by 10 list
maze[start_x][start_y] = steps
steps += 1

# Ask for ending position
while True:
    reply = input("What row is the exit in? 0-9\n")
    if not reply.isnumeric():
        print("Error! Make sure you enter only an integer")
    elif int(reply) < 0 or int(reply) > 9:
        print("Error! Make sure you only enter a value between 0 and 9 inclusive")
    else:
        end_x = int(reply)
        break

while True:
    reply = input("What column is the exit in? 0-9\n")
    if not reply.isnumeric():
        print("Error! Make sure you enter only an integer")
    elif int(reply) < 0 or int(reply) > 9:
        print("Error! Make sure you only enter a value between 0 and 9 inclusive")
    else:
        end_y = int(reply)
        break

# Asking for which direction
while True:
    reply = input("Which way are you facing?\nPlease Enter either North, East, South or West\n")
    if reply not in directions :
        print("Error! Make sure you enter one of the given directions")
    else:
        facing = reply
        break

# Marking exit on 10 by 10 list
maze[end_x][end_y] = 101

# Mapping out the maze (WORK IN PROGRESS)
x = start_x
y = start_y

while (x != end_x) and (y != end_y):
    while True:
        reply = input("Did you take a step forward? Yes or No\n")
        if reply.strip() != "Yes" and reply.strip() != "No":
            print("Error! Make sure you only enter either Yes or No")
        elif reply.strip() == "Yes":
            maze[x][y] = steps
            steps += 1
            break

        else:
            while True:
                reply = input("Will you be turning left or right? Left or Right\n")
                if reply.strip() != "Left" or reply != "Right":
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

# Prints out the 2-D maze
for i in range(0, ROW):
    for j in range(0, COL):
        print(str(maze[i][j]), end=" ")
    print("")
