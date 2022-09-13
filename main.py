# basic mouse tracker app

import pygame as pg

# mouse class
import pygame.draw


class Mouse:

    # get mouse pos
    def show_mouse_position(self):
        mouse_pos = pg.mouse.get_pos()
        print(f'mouse pos is {mouse_pos[0], mouse_pos[1]}')
        return mouse_pos

    def get_position(self):
        mouse_pos = pg.mouse.get_pos()
        return mouse_pos

    def draw_vertical_line(self, start_x):
        pygame.draw.line(screen, (10,110,10), (start_x, 0), (start_x, 800), 1)

    def draw_horizontal_line(self, start_y):
        pygame.draw.line(screen, (10,110,10), (0, start_y), (800, start_y), 1)

class Screen:

    def __init__(self):
        self.x = 800
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen


# init screen
s = Screen()
screen = s.set_mode()

mouse = Mouse()

while True:
    screen.fill((0, 0, 0))

    mouse.draw_vertical_line(mouse.get_position()[0])
    mouse.draw_horizontal_line(mouse.get_position()[1])


    for event in pg.event.get():
        # player movement
        if event.type == pg.MOUSEMOTION:
            mouse.show_mouse_position()
            mouse.draw_vertical_line(mouse.get_position()[0])
            mouse.draw_horizontal_line(mouse.get_position()[1])
            pg.display.update()

    pg.display.update()
