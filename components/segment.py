from lib.include import set_relative
from lib.values import PIXEL_SIZE
import pygame as pg

class segment:
    def __init__(self, color,  mother=None, child=None, current_position=None, current_direction=None):
        self.color = color
        self.mother = mother
        self.child = child
        self.current_position = current_position
        self.current_direction = current_direction

    def show(self, window):
        relative_position = set_relative(self.current_position)
        return pg.draw.rect(window, self.color, [relative_position[0], relative_position[1], PIXEL_SIZE[0],
                                                 PIXEL_SIZE[1]])

    def pass_info(self, debug=False):
        self.child.current_position = self.current_position
        if debug:
            print(f"Me is {self}\tMother is {self.mother}\t Child is {self.child}")
            print(f" me position is {self.current_position}\tChild position is {self.child.current_position}\n\n")



class head(segment):

    def __init__(self, size, current_position, win, current_direction, previous_direction, color):
        super().__init__(color=color)
        self.size = size
        self.current_position = current_position
        self.win = win
        self.current_direction = str(current_direction)
        self.previous_direction = str(previous_direction)

    def draw_head(self, window):
        self.position_checks()
        relative_position = set_relative(self.current_position)
        return pg.draw.rect(window, self.color, [relative_position[0],
                                            relative_position[1],
                                            self.size[0],
                                            self.size[1]])

    def position_checks(self):
        if self.current_position[0] < 0:
            self.current_position[0] = self.win.w_size[0] - PIXEL_SIZE[0]
        elif self.current_position[0] > self.win.w_size[0] - PIXEL_SIZE[0]:
            self.current_position[0] = 0
        if self.current_position[1] > self.win.w_size[1] - PIXEL_SIZE[1]:
            self.current_position[1] = 0
        elif self.current_position[1] < 0:
            self.current_position[1] = self.win.w_size[1] - PIXEL_SIZE[1]
