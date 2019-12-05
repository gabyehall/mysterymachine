#if breeze detected, adjusts squares
def breeze(board, cur_y, cur_x):
    board[cur_y][cur_x] += "B "
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Ph "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Ph "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Ph "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Ph "
    return board

#if smell detected, adjusts squares
def smell(board, cur_y, cur_x):
    board[cur_y][cur_x] += "Sm "
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Pw "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Pw "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Pw "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Pw "
    return board

#if glitter detected, adjusts squares
def glitter(board, cur_y, cur_x):
    board[cur_y][cur_x] += "Gl "
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Pg "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Pg "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Pg "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Pg "
    return board

#if no breeze detected, adjusts squares
def no_breeze(board, cur_y, cur_x):
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Nh "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Nh "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Nh "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Nh "
    return board

#if no smell detected, adjusts squares
def no_smell(board, cur_y, cur_x):
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Ns "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Ns "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Ns "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Ns "
    return board

#if no glitter detected, adjusts squares
def no_glitter(board, cur_y, cur_x):
    if cur_y-1 > -1:
        board[cur_y-1][cur_x] += "Ng "
    if cur_y+1 < 4:
        board[cur_y+1][cur_x] += "Ng "
    if cur_x-1 > -1:
        board[cur_y][cur_x-1] += "Ng "
    if cur_x+1 < 4:
        board[cur_y][cur_x+1] += "Ng "
    return board

#check if 2 or more possibles for a space, convert to certain
def check_2(board, cur_y, cur_x):
    hole_check = board[cur_y][cur_x].count("Ph ")
    wump_check = board[cur_y][cur_x].count("Pw ")
    gold_check = board[cur_y][cur_x].count("Pg ")
    if hole_check>1:
        board[cur_y][cur_x] = "Ch "
    elif wump_check>1:
        board[cur_y][cur_x] = "Cw "
    elif gold_check>1:
        board[cur_y][cur_x] = "Cg "
    return board  

#check-2 applied to entire board
def check_2_board(board):
    for i in range(4):
        for j in range(4):
            board = check_2(board,i,j)
    return board    
    
#checks if an Nw and an Np, and changes to S
#if there is an S, then clears all other variables
def safe_check(board):
    for i in range(4):
        for j in range(4):
            nw_count = board[i][j].count("Nw ")
            np_count = board[i][j].count("Np ")
            if nw_count>0 and np_count>0:
                board[i][j] += "S "
            
            s_count = board[i][j].count("S ")
            if s_count>0:
                board[i][j] = "S "
    return board

def n_check(board):
    for i in range(4):
        for j in range(4):
            nh_count = board[i][j].count("Nh ")
            if nh_count>0:
                board[i][j].replace("Ph ","")
            
            nw_count = board[i][j].count("Nw ")
            if nw_count>0:
                board[i][j].replace("Pw ","")
            
            ng_count = board[i][j].count("Ng ")
            if ng_count>0:
                board[i][j].replace("Pg ","")
    return board

def wumpus_check(board):
    for i in range(4):
        for j in range(4):
            pw_count = board[i][j].count("Pw ")
            if pw_count>=2:
                board[i][j].replace("Pw ","")
                board[i][j] +=  "Dw "
    return board
            

#determine if a tile is a corner, edge, or inner tile
def determine_tile_type(board, cur_y, cur_x):
    if cur_y==0 or cur_y==3 or cur_x==0 or cur_y==3:
        if cur_y==0 and cur_x==0:
            tile_type = "corner"
        elif cur_y==0 and cur_x==3:
            tile_type = "corner"
        elif cur_y==3 and cur_x==0:
            tile_type = "corner"
        elif cur_y==3 and cur_x==3:
            tile_type = "corner"
        else:
            tile_type = "edge"
    else:
        tile_type = "inner"
    return tile_type

#input sense as a list (if multiple inputs)
#runs through all the logic to update the board
#WORK IN PROGRESS - WILL THERE BE MULTIPLE INPUTS? (will aftect 'N' statements)
def run_round(board, sense, cur_y, cur_x):
    if "" in sense:
        board[cur_y][cur_x] = "S "
    if "breeze" in sense:
        board = breeze(board, cur_y, cur_x)
    if "smell" in sense:
        board = smell(board, cur_y, cur_x)
    if "glitter" in sense:
        board = glitter(board, cur_y, cur_x)
    if "breeze" not in sense and sense!="":
        board = no_breeze(board, cur_y, cur_x)
    if "smell" not in sense and sense!="":
        board = no_smell(board, cur_y, cur_x)
    if "glitter" not in sense and sense!="":
        board = no_glitter(board, cur_y, cur_x)
    board = n_check(board)
    board = safe_check(board)
    board = wumpus_check(board)
    board = check_2_board(board)
    return board

#prints the board - NO RETURN
def print_board(board):
    print("\n")
    for i in range(4):
        for j in range(4):
            print("{:<10}".format(board[i][j]),end="")
        print("")





#####SET FIRST TILE (STARTING TILE) EQUAL TO "S "#####
tile_board = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]

for i in range(4):
    for j in range(4):
        tile_board[i][j] = (".")


#starting coordinates
x = 0
y = 3
print_board(tile_board)
tile_board[y][x] += "S "

#main simulator
while True:
    direction = ""
    sensed = ""
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    if x==-1:
        break
    
    sensed = input("Enter sense: ")
    tile_board = run_round(tile_board, sensed, y, x)
    
    print_board(tile_board)
    print("CURRENT X:",x)
    print("CURRENT Y:",y)