
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
       # drone.throttle(int(leftstick))
    
    if Start == 1:
        print('Start pressed')
        drone.takeoff1()
    
    if Back == 1:
        drone.land()
        print('Back pressed')
    if abs(leftsticky) > .05:
       
        drone.pitch1(-leftsticky)
  
    if abs(rightsticky) > .05:
      
        drone.throttle1(-rightsticky)

    if abs(leftstickx) > .05:
       
        drone.roll1(leftstickx)
    if abs(rightstickx) > .05:
    
        drone.yaw1(rightstickx)
        
    sleep(.02)







