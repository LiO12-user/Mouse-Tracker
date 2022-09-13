# basic mouse tracker app

import pygame as pg


# mouse class
class Mouse:

    # get mouse pos
    def get_position(self):
        mouse_pos = pg.mouse.get_pos()
        print(f'mouse pos is {mouse_pos[0], mouse_pos[1]}')
        return mouse_pos


class Screen:

    def __init__(self):
        self.x = 900
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen


# init screen
s = Screen()
screen = s.set_mode()

mouse = Mouse()

while True:

    for event in pg.event.get():
        # player movement
        if event.type == pg.MOUSEMOTION:
            mouse.get_position()

    pg.display.update()
