# coding=utf-8
# Pong -> Control

import pygame.event as event
import pygame.locals as pl

# Can be overwritten by main?
mappings = {
    pl.K_UP: "UP",
    pl.K_DOWN: "DOWN",
    pl.K_RETURN: "START" }

model = {
    "UP": False,
    "DOWN": False,
    "START": False,
    "QUIT": False }

# XXX Untested
def input_list(feed=event.get):
    """Return a list of player inputs represented as strings.
    The complete list of options is found in control.mappings.
    """

    inputs = []
    for e in event.get():
        if e.type == pl.KEYDOWN:
            if e.key in mappings.keys():
                inputs.append(mappings[e.key])
            else:
                pass
        elif e.type == pl.KEYUP:
            pass  # Not sure what to do here...
        elif e.type == pl.QUIT:
            inputs.append("QUIT")
    return inputs


# XXX Untested
def input_model(feed=event.get):
    """Return a dictionary representing a model of a controller.
    Each key represents one button or input (implemented as an input string)
    and maps to a boolean indicating whether it is currently pressed or not.

    This function is mututally exclusive with control.input_list -- do not
    use both in the same loop. They will eat each other's input.
    """

    global model
    for e in feed():
        if e.type == pl.KEYDOWN:
            if e.key in mappings.keys():
                model[mappings[e.key]] = True
            else:
                pass
        elif e.type == pl.KEYUP:
            if e.key in mappings.keys():
                model[mappings[e.key]] = True
            else:
                pass
        elif e.type == pl.QUIT:
            model["QUIT"] = True
    return model
