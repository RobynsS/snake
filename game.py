import random

import objects
import canvas


class Game:
    def __init__(self, width, height):
        self.grid = canvas.Grid(height, width)
        self.snake = objects.Snake(canvas.Point((round(width / 2) - 1), (round(height / 2)) - 1),
                                   objects.Direction.RIGHT)
        self.apples = []

    def update(self):
        self.snake.move()
        self.create_apple()

    def process_input(self, key):
        if key == 'UP':
            self.snake.direction = objects.Direction.UP
        elif key == 'RIGHT':
            self.snake.direction = objects.Direction.RIGHT
        elif key == 'LEFT':
            self.snake.direction = objects.Direction.LEFT
        elif key == 'DOWN':
            self.snake.direction = objects.Direction.DOWN
        # TODO: make it impossible to make a 360° turn

    def create_apple(self):
        if not self.apples:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            self.apples.append(objects.Apple(canvas.Point(x, y)))
