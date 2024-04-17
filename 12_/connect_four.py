grid = [
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
]

current_piece = "R"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 7:
                print(grid[row][col], end="   ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 8):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def get_row(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3 or grid_spot == 4 or grid_spot == 5 or grid_spot == 6 or grid_spot == 7 or grid_spot == 8:
        return 4 
    #elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
    #    return 1
    #else:
    #    return 2    

def get_col(grid_spot):
    if grid_spot == 1:
        return 0
    elif grid_spot == 2:
        return 1
    elif grid_spot == 3:
        return 2
    elif grid_spot == 4:
        return 3
    elif grid_spot == 5:
        return 4
    elif grid_spot == 6:
        return 5
    elif grid_spot == 7:
        return 6
    elif grid_spot == 8:
        return 7
    #if grid_spot == 1 or grid_spot == 4 or grid_spot == 7:
    #    return 0
    #elif grid_spot == 2 or grid_spot == 5 or grid_spot == 8:
    #    return 1
    #else:
    #    return 2
    
def place_piece(grid_spot : int):
    while(True):
        row = get_row(grid_spot)
        col = get_col(grid_spot)
        grid_value = grid[row][col]
        if (not grid_value.__eq__("R") and not grid_value.__eq__("Y")):
            break
        user_choice = ""
        while (is_bad_num_string(user_choice)):
            user_choice = input("Enter a number (1-8) where to put the piece: ")
        grid_spot = int(user_choice)
    grid[row][col] = current_piece 
 
def check_row_for_win():
    for row in range(len(grid)):
        current_row = grid[row]
        if current_row[0].__eq__(current_row[1]) and current_row[1].__eq__(current_row[2]) and current_row[2].__eq__(current_row[3]) and current_row[3].__eq__(current_row[4]):
            return True
    return False


def check_col_for_win():
    for col in range(7):
        if grid[0][col].__eq__(grid[1][col]) and grid[1][col].__eq__(grid[2][col]) and grid[2][col].__eq__(grid[3][col]) and grid[3][col].__eq__(grid[4][col])and grid[4][col].__eq__(grid[5][col]) and grid[5][col].__eq__(grid[6][col]) and grid[6][col].__eq__(grid[7][col]):
            return True
    return False

def check_left_diag_for_win():
    return grid[0][0].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][2]) 


def check_right_diag_for_win():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    for row in range(4):
        for col in range(7):
            if grid[row][col].isnumeric():
               return False
    return True
        
 
def check_end():
    if(check_row_for_win()):
        print(current_piece + " wins!")
        return True
    elif(check_col_for_win()):
        print(current_piece + " wins!")
        return True
    elif(check_left_diag_for_win()):
        print(current_piece + " wins!")
        return True
    elif(check_right_diag_for_win()):
        print(current_piece + " wins!")
        return True
    elif(check_draw()):
        print("The game is a draw")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to Connect Four")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-8) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_end()):
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print_grid()
    print("GAME OVER")
        
game_loop()