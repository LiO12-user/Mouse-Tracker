# basic mouse tracker app
import pygame as pg
import pygame.font

import pygame.draw

pygame.font.init()


# mouse class
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
        pygame.draw.line(screen, (10, 110, 10), (start_x, 0), (start_x, 800), 1)

    def draw_horizontal_line(self, start_y):
        pygame.draw.line(screen, (10, 110, 10), (0, start_y), (800, start_y), 1)


class Axis:
    def __init__(self):
        self.y_axis_array = [200]
        self.x_axis_array = [200]



    pass


class Screen:

    def __init__(self):
        self.x = 800
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen


class Texts:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def show_text(self, text, x, y):
        over_text = self.font.render(str(text), True, (255, 255, 255))
        screen.blit(over_text, (x, y))


text = Texts()

# init screen
s = Screen()
screen = s.set_mode()

mouse = Mouse()


while True:
    screen.fill((0, 0, 0))

    mouse.draw_vertical_line(mouse.get_position()[0])
    mouse.draw_horizontal_line(mouse.get_position()[1])

    text.show_text(f'x pos: {mouse.get_position()[0]}', 20, 20)
    text.show_text(f'y pos: {mouse.get_position()[1]}', 20, 50)

    for event in pg.event.get():
        # player movement
        if event.type == pg.MOUSEMOTION:
            mouse.show_mouse_position()
            mouse.draw_vertical_line(mouse.get_position()[0])
            mouse.draw_horizontal_line(mouse.get_position()[1])
            pg.display.update()
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.draw.lines(screen, (10, 110, 10), False, [(200, 300), (500, 600)] ,20)
            # mouse_x, mouse_y = mouse.get_position()[0], mouse.get_position()[1]

    pg.display.update()
