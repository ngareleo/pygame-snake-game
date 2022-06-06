from lib import *
from components import *
import pygame as pg
from game import Game

pg.init()

def initialize_components():
    game_window = SnakeWindow(
        w_size=PLAY_WINDOW_SIZE,
        background_color=WHITE,
    )
    main_window = pg.display.set_mode(WINDOW_SIZE)
    spawn_point = [WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]
    game_snake = Snake(
        size=PIXEL_SIZE,
        current_position=spawn_point,
        window=game_window,
        current_direction="e", # TODO Use an enumerator
        previous_direction="n", # TODO Use an enumerator
        color=random_color(),
        sgl=[],
    )
    return (game_window, main_window, game_snake) 

    
def main():

    game_running = True
    game_window, main_window, game_snake = initialize_components()
    game = Game(
        main_window=main_window,
        window=game_window,
        snake=game_snake,
        score=0,
        timer=0,
        score_board=ScoreBoard()
    )

    snake_head = game_snake.snake_head

    pg.display.set_caption(WINDOW_TITLE)
    while game_running:
        game.setup()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        res = event_listener(snake_head.current_direction, snake_head.current_position)
        game_snake.pass_to_child()
        res[0] = snake_head.current_position
        if valid_direction_change(direction=res[1],
                                  current_direction=snake_head.current_direction,
                                  snake_head_only=game_snake.get_number_of_segments() == 0):
            snake_head.previous_direction = snake_head.current_direction
            snake_head.current_direction = res[1]
        else:
            snake_head.current_position = map_direction_change(snake_head.current_direction,
                                                               snake_head.current_position)
        pg.display.update()


if __name__ == '__main__':
    main()
