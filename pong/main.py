#There are 2 paddles, there is one ball
#if the ball touches the side of the screen of a player
#the other player gets a point.
#If the ball hits a paddle it bounces off, maintaining its momentum
#First to a certain number of points wins
#Computer AI
#Strong Separation of concerns
#main module (game loop)
#Display module 
#Input module
#game logic module 
    #submodule for number crunching
#Style guide

import pygame
import display


def init():
    pygame.init()
    pygame.display.set_mode((700, 500))

init()

"""def loop():
    control.get_input()
    logic.process_input()
    display.show_display()  
    pass"""



"""display-
all active rectangles
scores
menus
text stuff

input-
start input
up/down
pause

logic-
contains squares in play

control-
make stuff happen"""


