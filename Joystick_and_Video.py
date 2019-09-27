
# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain 

from __future__ import division
import pygame
from time import sleep
import os
from app.TEST import Drone
# This is set because normally pygame uses this video drive but the google coral does not support it
drone = Drone()

pygame.init()

drone.video()

joystick_count = pygame.joystick.get_count()
speed = 50
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print('init')

while True:
    pygame.event.get()

    if joystick_count != 0:
        rightsticky = gamepad.get_axis(1)
        leftsticky = gamepad.get_axis(4)

        rightstickx = gamepad.get_axis(0)
        leftstickx = gamepad.get_axis(3)
        Start = gamepad.get_button(7)
        Back = gamepad.get_button(6)
        x, y = gamepad.get_hat(0)
        # down = gamepad.get_axis(6)
        # left  = gamepad.get_hat(3)
        # right = gamepad.get_hat(4)

    # print(x, "x")
    # print(y)
  
   
    
    
    
    if Start == 1:
        print('Start pressed')
        drone.takeoff1()
    
    if Back == 1:
        drone.land()
        print('Back pressed')
    if abs(leftsticky) > .05:
       
        drone.pitch(-leftsticky)
    else:
        drone.pitch(0)
    if abs(rightsticky) > .05:
      
        drone.throttle(-rightsticky)
    elif y != 0:
        drone.throttle(y)
    
    else:
        drone.throttle(0)
    if abs(leftstickx) > .05:
        print("call")
        drone.roll(leftstickx)
    else:
        drone.roll(0)
    if abs(rightstickx) > .05:
    
        drone.yaw(rightstickx)
    elif x != 0:
        drone.yaw(x)
    else:
        drone.yaw(0)
    
    sleep(.02)







