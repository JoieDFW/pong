# coding=utf-8
# Pong -> Tests -> Control

import pygame.locals as pl
from pong.control import input_list, input_model

def test_input_list():
    mockFeed = lambda: [pl.K_UP, pl.K_w, pl.K_RETURN]
    output = input_list(feed=mockFeed)
     
def test_input_model():
    mockFeed = lambda: [pl.K_UP, pl.K_w, pl.K_RETURN]
    model = input_model(feed=mockFeed)
    
