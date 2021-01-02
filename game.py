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
        self.correct_snake_on_grid()
        self.create_apple()

    def correct_snake_on_grid(self):
        snake_head = self.snake.get_head()
        if snake_head.x >= self.grid.width or snake_head.x < 0:
            snake_head.x = snake_head.x % self.grid.width
        if snake_head.y >= self.grid.height or snake_head.y < 0:
            snake_head.y = snake_head.y % self.grid.height

        self.snake.set_head(snake_head)

    def process_input(self, value):
        if value in {'UP', 'RIGHT', 'DOWN', 'LEFT'}:
            direction = None
            if value == 'UP':
                direction = objects.Direction.UP
            elif value == 'RIGHT':
                direction = objects.Direction.RIGHT
            elif value == 'LEFT':
                direction = objects.Direction.LEFT
            elif value == 'DOWN':
                direction = objects.Direction.DOWN

            self.snake.set_direction(direction)

    def create_apple(self):
        if not self.apples:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            self.apples.append(objects.Apple(canvas.Point(x, y)))
