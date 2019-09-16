
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
    if A == 1:
        print('A pressed')
    if B == 1:
        print('B pressed')
    if Y == 1:
        print('Y pressed')

    if LB == 1:
        print('LB pressed')
    if RB == 1:
        print('RB pressed')
 
    if Start == 1:
        drone.takeoff()
        print('Start pressed')
    if Back == 1:
        drone.land()
        print('Back pressed')
    

#     forward
# backward
# left
# right
# up
# down
# clockwise
# counter_clockwise

    if  abs(leftsticky) > .05:
        if leftsticky > .05:
            drone.down(leftsticky * speed)
        else:
            drone.up(-leftsticky * speed)

    if  abs(rightsticky) > .05:
        if rightsticky > .05:
            drone.backward(rightsticky * speed)
        else:
            drone.forward(-rightsticky * speed)
       
    if  abs(leftstickx) > .05:
        if leftstickx > .05:
            drone.clockwise(leftstickx * speed)

        else:
            drone.counter_clockwise(-leftstickx * speed)
        
    if  abs(rightstickx) > .05:
        if leftsticky > .05:
            drone.right(rightstickx * speed)

        else:
            drone.left(-rightstickx * speed)
        
    sleep(.05)







