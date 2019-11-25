#!/usr/bin/env python3
import os
import sys
from time import *
from ev3dev.ev3 import *
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4


os.system('setfont Lat15-TerminusBold14')
mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'

gun = MediumMotor('outA'); gun.stop_action = 'hold'


print('Hello, my name is EV3!')
Sound.speak('Hello master Bram, I am the mystery machine!').wait()

#Shooting Joey's Gun 
gun.on(100)
sleep(5)
gun.off()

mL.run_to_rel_pos(position_sp= 520, speed_sp = 500)
mR.run_to_rel_pos(position_sp= 520, speed_sp = 500)
mL.wait_while('running')
mR.wait_while('running')


#fugure 8












