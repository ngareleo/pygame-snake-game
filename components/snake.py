from .segment import segment, head
from lib.include import random_color

class Snake:

    def __init__(self, size, current_position, window, current_direction, previous_direction, color, sgl):
        self.snake_head = head(
            size=size,
            current_position=current_position,
            win=window,
            current_direction=current_direction,
            previous_direction=previous_direction,
            color=color 
        )
        self.sgl = list(sgl)

    def show_info(self):
        # position, children
        snake_head = self.snake_head
        segments = self.sgl
        print(f"Current position : {snake_head.current_position}")
        print(f"Current direction : {snake_head.current_direction}")
        print(f"Current children are {segments}")
        for seg in segments:
            print(f"{seg.current_position}")

    def render_snake(self, window):
        self.snake_head.draw_head(window)
        for ss in self.sgl:
            ss.show(window)

    def add_child(self):
        if len(self.sgl) == 0:
            self.sgl.append(segment(mother=self.snake_head, color=random_color()))
            self.snake_head.child = self.sgl[0]
            return
        new_segment = segment(color=random_color())
        new_segment.mother = self.sgl[-1]
        self.sgl[-1].child = new_segment
        self.sgl.append(new_segment)

    def pass_to_child(self):
        if len(self.sgl) == 0:
            return
        snake_head = self.sgl[-1]
        while snake_head.mother:
            snake_head.current_position = snake_head.mother.current_position
            snake_head = snake_head.mother

    def get_number_of_segments(self):
        return len(self.sgl)
