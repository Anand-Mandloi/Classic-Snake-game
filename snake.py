from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    segment_list = []

    def __init__(self):
        self.create_snake()


    def create_snake(self):
        for i in range(20, -100, -20):
            new_segment = Turtle(shape='square')
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i, 0)

            self.segment_list.append(new_segment)
            self.head = self.segment_list[0]

    def add_segment(self):
        new_segment = Turtle(shape='square')
        new_segment.color("white")
        new_segment.penup()
        snake_len = len(self.segment_list)
        new_segment.goto(self.segment_list[-1].position())
        self.segment_list.append(new_segment)

    def reset_game(self):
        for seg in self.segment_list:
            seg.goto(2000, 2000)
        self.segment_list.clear()
        self.create_snake()

    def move_snake(self, step):
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.segment_list[i].goto(self.segment_list[i - 1].position())

        self.head.forward(step)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def collision_with_tail(self):
        for i in range(1, len(self.segment_list), 1):
            if self.head.distance(self.segment_list[i]) <= 15:
                return True
        return False
