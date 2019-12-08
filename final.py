#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

#use this to run the code
"""RIGHT CLICK 'VELMA' AND CLICK OPEN SSH TERMINAL"""
"""TYPE THESE IN:"""
#cd vscode-hello-python-master
#brickrun -r ./final.py



import os
import sys
from time import *

# state constants
ON = True
OFF = False

def forward(left_motor, right_motor):
    left_motor.on(-40)
    right_motor.on(-40)
    sleep(2)
    left_motor.off()
    right_motor.off()

def right(left_motor, right_motor):
    left_motor.on(15)
    right_motor.on(-15)
    sleep(2)
    left_motor.off()
    right_motor.off()

def left(left_motor, right_motor):
    left_motor.on(-15)
    right_motor.on(15)
    sleep(2)
    left_motor.off()
    right_motor.off()

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font
    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')

    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)

    #!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

os.system('setfont Lat15-TerminusBold14')
mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'

gun = MediumMotor('outA'); gun.stop_action = 'hold'


#if breeze detected, adjusts squares
def breeze(board, cur_y, cur_x, hole_count):
    if "x" in board[cur_y][cur_x]:
        return board
    else:
        board[cur_y][cur_x] += "B "
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += str(hole_count)+"Ph "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += str(hole_count)+"Ph "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += str(hole_count)+"Ph "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += str(hole_count)+"Ph "
        board[cur_y][cur_x] += "x "
        return board

#if smell detected, adjusts squares
def smell(board, cur_y, cur_x):
    if "x" in board[cur_y][cur_x]:
        return board
    else:    
        board[cur_y][cur_x] += "Sm "
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += "Pw "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += "Pw "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += "Pw "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += "Pw "
        board[cur_y][cur_x] += "x "
        return board

#if glitter detected, adjusts squares
def glitter(board, cur_y, cur_x):
    if "x" in board[cur_y][cur_x]:
        return board
    else:
        board[cur_y][cur_x] += "Gl "
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += "Pg "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += "Pg "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += "Pg "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += "Pg "
        board[cur_y][cur_x] += "x "
        return board

#if no breeze detected, adjusts squares
def no_breeze(board, cur_y, cur_x):
    if "x" in board[cur_y][cur_x]:
        return board
    else:
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += "Nh "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += "Nh "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += "Nh "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += "Nh "
        board[cur_y][cur_x] += "x "
        return board

#if no smell detected, adjusts squares
def no_smell(board, cur_y, cur_x):
    if "x" in board[cur_y][cur_x]:
        return board
    else:
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += "Ns "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += "Ns "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += "Ns "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += "Ns "
        board[cur_y][cur_x] += "x "
        return board

#if no glitter detected, adjusts squares
def no_glitter(board, cur_y, cur_x):
    if "x" in board[cur_y][cur_x]:
        return board
    else:
        if cur_y-1 > -1:
            board[cur_y-1][cur_x] += "Ng "
        if cur_y+1 < 4:
            board[cur_y+1][cur_x] += "Ng "
        if cur_x-1 > -1:
            board[cur_y][cur_x-1] += "Ng "
        if cur_x+1 < 4:
            board[cur_y][cur_x+1] += "Ng "
        board[cur_y][cur_x] += "x "
        return board

#check if 2 or more possibles for a space, convert to certain
def check_2(board, cur_y, cur_x):
    hole_check = board[cur_y][cur_x].count("Ph ")
    wump_check = board[cur_y][cur_x].count("Pw ")
    gold_check = board[cur_y][cur_x].count("Pg ")
    
    #check if more than one possibility in each
    poss_count = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    
    for i in range(4):
        for j in range(4):
            cur_poss_count = board[i][j].count("P")
            poss_count[i][j] = cur_poss_count
        
    if hole_check>1:
        pre_overlap = set(board[cur_y][cur_x].strip(".").split(" "))
        for i in range(4):
            for j in range(4):
                current_overlap = set(board[i][j].strip(".").split(" "))
                overlap = list(pre_overlap&current_overlap)
                overlap = str(overlap).replace("'","").replace(",","").replace("[","").replace("]","")
                overlap_count = overlap.count("Ph")
                cur_tile_type = determine_tile_type(board, i, j)
                if overlap_count>0 and cur_y!=i and cur_x!=j and (cur_tile_type=="edge" or cur_tile_type=="corner"):
                    board[i][j] = str(board[i][j]).replace("Ph","")
        board[cur_y][cur_x] = "Ch "
    elif wump_check>1:
        board[cur_y][cur_x] = "Cw "
    elif gold_check>1:
        board[cur_y][cur_x] = "Cg "
    
    #complete check for possibilities becoming certain if other possiblity removed
    for i in range(4):
        for j in range(4):
            cur_poss_count = board[i][j].count("P")
            if cur_poss_count<poss_count[i][j] and cur_poss_count==1:
                board[i][j].replace("P","C")
    
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
def run_round(board, sense, cur_y, cur_x, hole_count):
    if "" in sense:
        board[cur_y][cur_x] = "S "
        if cur_y-1>=0:
            board[cur_y-1][cur_x] = "S "
        if cur_y+1<=3:
            board[cur_y+1][cur_x] = "S "
        if cur_x-1>=0:
            board[cur_y][cur_x-1] = "S "
        if cur_x+1>=0:
            board[cur_y][cur_x+1] = "S "
    if "breeze" in sense:
        board = breeze(board, cur_y, cur_x, hole_count)
        hole_count += 1
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
    return board, hole_count

#prints the board - NO RETURN
def print_board(board):
    print("\n")
    for i in range(4):
        for j in range(4):
            print("{:<10}".format(board[i][j]),end="")
        print("")

#moves the robot based on direction to move and current direction it is facing
def move(direction, facing, mL, mR):
    if facing=="up":
        if direction=="left":
            left(mL,mR)
        elif direction=="right":
            right(mL,mR)
        elif direction=="up":
            pass
        elif direction=="down":
            right(mL,mR)
            right(mL,mR)
    elif facing=="down":
        if direction=="left":
            right(mL,mR)
        elif direction=="right":
            left(mL,mR)
        elif direction=="up":
            right(mL,mR)
            right(mL,mR)
        elif direction=="down":
            pass
    elif facing=="right":
        if direction=="left":
            right(mL,mR)
            right(mL,mR)
        elif direction=="right":
            pass
        elif direction=="up":
            left(mL,mR)
        elif direction=="down":
            right(mL,mR)
    elif facing=="right":
        if direction=="left":
            right(mL,mR)
            right(mL,mR)
        elif direction=="right":
            pass
        elif direction=="up":
            left(mL,mR)
        elif direction=="down":
            right(mL,mR)
    return direction

#check if robot is in a tile surrounding the wumpus
#returns direction that robot must point to shoot at it
def wumpus_surround(cur_x, cur_y, w_x, w_y):
    if (cur_x==(w_x+1) and cur_y==w_y):
        return "left"
    elif (cur_x==(w_x-1) and cur_y==w_y):
        return "right" 
    elif (cur_x==(w_x) and cur_y==(w_y+1)):
        return "up"
    elif (cur_x==(w_x) and cur_y==(w_y-1)):
        return "down"
    else:
        return "none"


#applies the move function and automatically - makes robot move autonmously
def search(board, sense, cur_y, cur_x, hole_count, facing, mL, mR):
    board,hole_count = run_round(board, sense, cur_y, cur_x, hole_count)
    print(cur_y)

    cw_count = 0
    for i in range(4):
        for j in range(4):
            cw_count += board[i][j].count("Cw ")
    #generalized movement when unsure of where wumpus is
    if cw_count==0:
        if ("Ch" not in board[cur_y-1][cur_x]) and ("Ph" not in board[cur_y-1][cur_x]) and ("Pw" not in board[cur_y-1][cur_x]) and (cur_y-1>=0 and cur_y-1<=3):
            print("moving up")
            facing = move("up", facing, mL, mR)
            forward(mL, mR)
            cur_y -= 1
        else:
            if ("Ch" not in board[cur_y+1][cur_x]) and ("Ph" not in board[cur_y+1][cur_x]) and ("Pw" not in board[cur_y+1][cur_x]) and (cur_y+1>=0 and cur_y+1<=3):
                facing = move("down", facing, mL, mR)
                forward(mL, mR)
                cur_y += 1
            else:
                if ("Ch" not in board[cur_y][cur_x+1]) and ("Ph" not in board[cur_y][cur_x+1]) and ("Pw" not in board[cur_y][cur_x+1]) and (cur_x+1>=0 and cur_x+1<=3):
                    facing = move("right", facing, mL, mR)
                    forward(mL, mR)
                    cur_x += 1                
                else:
                    facing = move("left", facing, mL, mR)
                    forward(mL, mR)
                    cur_x -= 1
    #if Cw present in board, head toward that tile to kill it
    elif cw_count>0:
        w_x = 0
        w_y = 0
        for i in range(4):
            for j in range(4):
                if "Cw " in board[i][j]:
                    w_y = i
                    w_x = j
        #determine if in a space surrounding the wumpus
        surround = wumpus_surround(cur_x,cur_y,w_x,w_y)
        #get to wumpus via fastest route
        if surround=="none":
            if w_y<cur_y:
                if (("Ch" not in board[cur_y+1][cur_x]) and ("Ph" not in board[cur_y+1][cur_x]) and ("Pw" not in board[cur_y+1][cur_x])) and (cur_y+1>=0 and cur_y+1<=3):
                    facing = move("down", facing, mL, mR)
                    forward(mL, mR)
                    cur_y += 1
                else:
                    if ("Ch" not in board[cur_y][cur_x+1]) and ("Ph" not in board[cur_y][cur_x+1]) and ("Pw" not in board[cur_y][cur_x+1]) and (cur_x+1>=0 and cur_x+1<=3):
                        facing = move("right", facing, mL, mR)
                        forward(mL, mR)
                        cur_x += 1
                    else:
                        if ("Ch" not in board[cur_y-1][cur_x]) and ("Ph" not in board[cur_y-1][cur_x]) and ("Pw" not in board[cur_y-1][cur_x]) and (cur_y-1>=0 and cur_y-1<=3):
                            facing = move("up", facing, mL, mR)
                            forward(mL, mR)
                            cur_y -= 1
                        else:
                            facing = move("left", facing, mL, mR)
                            forward(mL, mR)
                            cur_x -= 1
            if w_y>cur_y:
                if ("Ch" not in board[cur_y-1][cur_x]) and ("Ph" not in board[cur_y-1][cur_x]) and ("Pw" not in board[cur_y-1][cur_x]) and (cur_y-1>=0 and cur_y-1<=3):
                    facing = move("up", facing, mL, mR)
                    forward(mL, mR)
                    cur_y += 1 
                else:
                    if ("Ch" not in board[cur_y][cur_x+1]) and ("Ph" not in board[cur_y][cur_x+1]) and ("Pw" not in board[cur_y][cur_x+1]) and (cur_x+1>=0 and cur_x+1<=3):
                        facing = move("right", facing, mL, mR)
                        forward(mL, mR)
                        cur_x += 1
                    else:
                        if ("Ch" not in board[cur_y+1][cur_x]) and ("Ph" not in board[cur_y+1][cur_x]) and ("Pw" not in board[cur_y+1][cur_x]) and (cur_y+1>=0 and cur_y+1<=3):
                            facing = move("down", facing, mL, mR)
                            forward(mL, mR)
                            cur_y += 1
                        else:
                            facing = move("left", facing, mL, mR)
                            forward(mL, mR)
                            cur_x -= 1
            if w_x<cur_x:
                if ("Ch" not in board[cur_y][cur_x-1]) and ("Ph" not in board[cur_y][cur_x-1]) and ("Pw" not in board[cur_y][cur_x-1]) and (cur_x-1>=0 and cur_x-1<=3):
                    facing = move("left", facing, mL, mR)
                    forward(mL, mR)
                    cur_x -= 1         
                else:
                    if ("Ch" not in board[cur_y-1][cur_x]) and ("Ph" not in board[cur_y-1][cur_x]) and ("Pw" not in board[cur_y-1][cur_x]) and (cur_y-1>=0 and cur_y-1<=3):
                        facing = move("up", facing, mL, mR)
                        forward(mL, mR)
                        cur_y -= 1
                    else:
                        if ("Ch" not in board[cur_y][cur_x+1]) and ("Ph" not in board[cur_y][cur_x+1]) and ("Pw" not in board[cur_y][cur_x+1]) and (cur_x+1>=0 and cur_x+1<=3):
                            facing = move("right", facing, mL, mR)
                            forward(mL, mR)
                            cur_x += 1
                        else:
                            facing = move("down", facing, mL, mR)
                            forward(mL, mR)
                            cur_y += 1                      
            if w_x>cur_x:                
                if ("Ch" not in board[cur_y][cur_x+1]) and ("Ph" not in board[cur_y][cur_x+1]) and ("Pw" not in board[cur_y][cur_x+1]) and (cur_x+1>=0 and cur_x+1<=3):
                    facing = move("right", facing, mL, mR)
                    forward(mL, mR)
                    cur_x += 1         
                else:
                    if ("Ch" not in board[cur_y-1][cur_x]) and ("Ph" not in board[cur_y-1][cur_x]) and ("Pw" not in board[cur_y-1][cur_x]) and (cur_y-1>=0 and cur_y-1<=3):
                        facing = move("up", facing, mL, mR)
                        forward(mL, mR)
                        cur_y -= 1
                    else:
                        if ("Ch" not in board[cur_y][cur_x-1]) and ("Ph" not in board[cur_y][cur_x-1]) and ("Pw" not in board[cur_y][cur_x-1]) and (cur_x-1>=0 and cur_x-1<=3):
                            facing = move("left", facing, mL, mR)
                            forward(mL, mR)
                            cur_x -= 1
                        else:
                            facing = move("down", facing, mL, mR)
                            forward(mL, mR)
                            cur_y += 1 
        else:
            move(surround, facing, mL, mR)
            gun.on(100)
            sleep(5)
            gun.off()
    
    for i in range(4):
        for j in range(4):
            if "Cg " in board[i][j]:
                if i==cur_y and j==cur_x:
                    facing = "STOP"
    
    return board,hole_count,facing,cur_y,cur_x







if __name__ == '__main__':
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')
    
    # print something to the screen of the device
    print('Hello World!')
    
    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')
    
    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)
    
    tile_board = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    
    for i in range(4):
        for j in range(4):
            tile_board[i][j] = (".")
    
    #starting coordinates
    x = 0
    y = 3
    print_board(tile_board)
    tile_board[y][x] += "S "
    
    hole_count = 1
    current_direction = "up"
    
    
    #main simulator
    while True:
        direction = ""
        sensed = ""
        
        sensed = input("Enter sense: ")
        tile_board, hole_count, current_direction, y, x = search(tile_board, sensed, y, x, hole_count, current_direction , mL, mR)
        
        print("facing:",current_direction)
        print("x",x)
        print("y",y)

        if current_direction=="STOP":
            print("puzzle solved!")
            break
        
        print_board(tile_board)