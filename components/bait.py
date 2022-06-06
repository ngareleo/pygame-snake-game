from lib.include import set_relative
import pygame as pg
from lib.values import RED, BAIT_RADIUS

class bait:

    def __init__(self, position, bait_timer):
        self.position = position
        self.bait_timer = bait_timer

    def render_bait(self, main_window):
        self.bait_timer = 100
        positions = set_relative(self.position)
        return pg.draw.rect(main_window, RED, [positions[0], positions[1], BAIT_RADIUS, BAIT_RADIUS])