from lib import *
from components import *
from random import randint

class Game:

    timer_helper = 0
    def __init__(self, main_window, window, snake, score, timer, score_board, rendered_bait=None):

        self.score = score
        self.window = window
        self.snake = snake
        self.rendered_bait = rendered_bait
        self.main_window = main_window
        self.score_board = score_board
        self.timer = timer

    def throw_bait(self):
        self.rendered_bait = bait(
            position=[randint(BAIT_RADIUS, PLAY_WINDOW_SIZE[0] - BAIT_RADIUS),
                      randint(BAIT_RADIUS, PLAY_WINDOW_SIZE[1] - BAIT_RADIUS)],
            bait_timer=100,
        )
        self.rendered_bait.render_bait(self.main_window)

    def show_bait(self):
        positions = set_relative(self.rendered_bait.position)
        return pg.draw.rect(self.main_window, RED, [positions[0], positions[1], BAIT_RADIUS, BAIT_RADIUS])

    def check_bait_timeout(self):
        if self.rendered_bait:
            self.show_bait()
            if self.rendered_bait.bait_timer < 0:
                self.rendered_bait = None
            else:
                self.rendered_bait.bait_timer -= 1

    def update_timer(self):
        self.timer_helper += 1
        if self.timer_helper == 10:
            self.timer_helper = 0
            self.timer += 1

    def check_collision(self):
        # bait has an enclosed-self space
        # we check if the head has by-passed the space
        game_snake = self.snake.snake_head
        bait_pos_limit = [
            [self.rendered_bait.position[0], self.rendered_bait.position[1]],
            [self.rendered_bait.position[0] + BAIT_RADIUS, self.rendered_bait.position[1]],
            [self.rendered_bait.position[0], self.rendered_bait.position[1] + BAIT_RADIUS],
            [self.rendered_bait.position[0] + BAIT_RADIUS, self.rendered_bait.position[1] + BAIT_RADIUS],
        ]
        snake_pos_limits = [
            [game_snake.current_position[0], game_snake.current_position[1]],
            [game_snake.current_position[0] + PIXEL_SIZE[0], game_snake.current_position[1]],
            [game_snake.current_position[0], game_snake.current_position[1] + PIXEL_SIZE[0]],
            [game_snake.current_position[0] + PIXEL_SIZE[0], game_snake.current_position[1] + PIXEL_SIZE[0]]

        ]

        return is_within(bait_pos_limit, snake_pos_limits, game_snake.current_direction)

    def self_collision(self):
        game_snake = self.snake.snake_head
        if len(self.snake.sgl) <= 4:
            return False
        for i in range(4, len(self.snake.sgl)):
            if self.snake.sgl[i].current_position == game_snake.current_position:
                print(f"Segment position is {self.snake.sgl[i].current_position}\tHead position is {game_snake.current_position}")
                self.reset_score()
                return True
        return False

    def game_over(self):
        pass

    def reset_score(self):
        self.score = 0
        self.timer = 0
        self.timer_helper = 0
        self.snake.sgl = []
        self.rendered_bait = None
        self.throw_bait()
        print("Game over")
        return

    def add_score(self):
        self.self_collision()
        if self.check_collision():
            self.score += 1
            self.rendered_bait = None
            self.snake.add_child()
            print(f"Score is {self.score}")

    def bait_exists(self):
        if not self.rendered_bait:
            self.throw_bait()

    def main_game_loop(self):
        game_snake = self.snake
        main_window = self.main_window
        game_snake.render_snake(main_window)
        # game_snake.show_info()
        self.bait_exists()
        self.add_score()
        self.check_bait_timeout()

    def setup(self):
        pg.time.delay(100)
        self.main_window.fill(WHITE)
        self.update_timer()
        self.score_board.update(self.score, self.timer)
        show_boundaries(self.main_window)
        self.score_board.render_board(self.main_window)
        self.main_game_loop()

