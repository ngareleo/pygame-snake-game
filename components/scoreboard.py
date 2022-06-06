from lib.include import set_placement
import pygame as pg
from lib.values import BLACK, WHITE

class ScoreBoard:

    def __init__(self, score=None, timer=None):
        self.score = score
        self.timer = timer

    def add_score(self):
        self.score += 1

    def update(self, score, time):
        self.score = score
        self.timer = time

    def render_board(self, window):
        font_used = pg.font.Font('freesansbold.ttf', 32)
        string = str(self.timer // 60) + " : " + str(self.timer % 60) + "   " + "Score : " + str(self.score)
        rendered_text = font_used.render(string, False, BLACK, WHITE)
        text_rect = rendered_text.get_rect()
        text_placement_info = set_placement()
        text_rect.center = text_placement_info[-1]

        window.blit(rendered_text, text_rect)
