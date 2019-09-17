
# Simple pygame test for the google coral
# Maps the gamepad for a Logitech controller
# Author: Danny Dasilva
# License: Public Domain 

from __future__ import division
import pygame
from time import sleep
import os
from app.Drone import Drone
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
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True   
    # D mode
    if joystick_count != 0:
        leftstickx = gamepad.get_axis(0)
        leftsticky = gamepad.get_axis(1)
        rightstickx = gamepad.get_axis(3)
        rightsticky = gamepad.get_axis(4)
        
        B = gamepad.get_button(1)
        X = gamepad.get_button(2)
        A = gamepad.get_button(0)
        Y = gamepad.get_button(3)
        LB = gamepad.get_button(4)
        RB = gamepad.get_button(5)
        Start = gamepad.get_button(7)
        Back = gamepad.get_button(6)

    
    if X == 1:
        print('X pressed')
        drone.left(speed)
    elif A == 1:
        print('A pressed')
        drone.backward(speed)
    elif B == 1:
        print('B pressed')
        drone.right(speed)
    elif Y == 1:
        print('Y pressed')
        drone.forward(speed)

    elif LB == 1:
        print('LB pressed')
    elif RB == 1:
        print('RB pressed')
 
    elif Start == 1:
        drone.takeoff()
        print('Start pressed')
    elif Back == 1:
        drone.land()
        print('Back pressed')
    

    elif  abs(leftsticky) > .05:
        if leftsticky > .05:
            drone.down(leftsticky * speed)
        else:
            drone.up(-leftsticky * speed)

    elif  abs(rightsticky) > .05:
        if rightsticky > .05:
            drone.backward(rightsticky * speed)
        else:
            drone.forward(-rightsticky * speed)
       
    elif  abs(leftstickx) > .05:
        if leftstickx > .05:
            drone.clockwise(leftstickx * speed)

        else:
            drone.counter_clockwise(-leftstickx * speed)
        
    elif  abs(rightstickx) > .05:
        if leftsticky > .05:
            drone.right(rightstickx * speed)

        else:
            drone.left(-rightstickx * speed)
    
    
        
    sleep(.02)







