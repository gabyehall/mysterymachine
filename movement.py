#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
from time import *

# state constants
ON = True
OFF = False

def forward(left_motor, right_motor):
    left_motor.on(40)
    right_motor.on(40)
    sleep(2)
    left_motor.off()
    right_motor.off()

def right(left_motor, right_motor):
    left_motor.on(12.5)
    right_motor.on(-12.5)
    sleep(2)
    left_motor.off()
    right_motor.off()

def left(left_motor, right_motor):
    left_motor.on(-12.5)
    right_motor.on(12.5)
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

"""print('Hello, my name is EV3!')
Sound.speak('Hello master Bram, I am the mystery machine!').wait()
mL.run_to_rel_pos(position_sp= 840, speed_sp = 500)
mR.run_to_rel_pos(position_sp= 840, speed_sp = 500)
mL.wait_while('running')
mR.wait_while('running')"""


#intiating the sensors
l1 = ColorSensor(INPUT_2)
l2 = ColorSensor(INPUT_3)

la = l1.reflected_light_intensity 
lb = l2.reflected_light_intensity 

print("la_initial",la)
print("lb_initial",lb)

forward(mL,mR)
right(mL,mR)
forward(mL,mR)
left(mL,mR)
forward(mL,mR)
left(mL,mR)
forward(mL,mR)
left(mL,mR)
forward(mL,mR)
left(mL,mR)
forward(mL,mR)
right(mL,mR)
forward(mL,mR)
right(mL,mR)
forward(mL,mR)

"""t = 0
while t=0:
    if(l1.reflected_light_intensity > la and l2.reflected_light_intensity() > lb):
        print('We are crossing spaces')
    else:
        mL.on(-8)
        mR.on(-8)
        print('We are in a grid space')

        print("l1",l1.reflected_light_intensity)
        print("l2",l2.reflected_light_intensity)
    sleep(1)
    t+=1"""

        


#if __name__ == '__main__':
    #main()
