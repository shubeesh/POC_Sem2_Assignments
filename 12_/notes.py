grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_grid():
    for number in range(len(grid)):
        print(grid[0], end = "")
        print("|", end = "")
        print (grid[1], end = "")
        print("|", end="")
        print(grid[number][2])
        if(number != 2):
            print("******")

def game_intro():
    print("Game has begun")

def game_loop():

    game_intro()

    while(True):
        user_request = input("Enter STOP to end the game, or other to continue")
        if user_request.__eq__ ("STOP"):
            break
        print("loop running")

    print("Game Over")

game_loop()



