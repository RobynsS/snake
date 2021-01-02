import random

import objects
import canvas


class Game:
    def __init__(self, width, height):
        self.grid = canvas.Grid(height, width)
        self.snake = objects.Snake(canvas.Point((round(width / 2) - 3), (round(height / 2) - 1)),
                                   canvas.Point((round(width / 2) - 2), (round(height / 2) - 1)),
                                   canvas.Point((round(width / 2 - 1)), (round(height / 2) - 1)),
                                   objects.Direction.RIGHT)
        self.food = []
        self.create_apple()
        self.growth_status = 0

    def update(self):
        if self.growth_status:
            self.snake.grow()
            self.growth_status = self.growth_status - 1
        else:
            self.snake.move()

        self.correct_snake_on_grid()

        eaten_food = self.snake_eats_food()
        if eaten_food:
            self.food.remove(eaten_food)
            self.growth_status = self.growth_status + 1
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

        # Get the points of free space where an apple can spawn
        free_space = []
        for i in range(0, self.grid.width):
            free_space.append([])
            for j in range(0, self.grid.height):
                free_space[i].append(True)

        for element in self.snake.elements:
            free_space[element.x][element.y] = False

        for piece in self.food:
            free_space[piece.pos.x][piece.pos.y] = False

        # Turn free space into list
        free_space_list = []
        for i in range(0, self.grid.width):
            for j in range(0, self.grid.height):
                if free_space[i][j]:
                    free_space_list.append(canvas.Point(i, j))

        if not self.food:
            random_index = random.randint(0, len(free_space_list) - 1)
            pos = free_space_list[random_index]
            self.food.append(objects.Apple(canvas.Point(pos.x, pos.y)))


    def snake_eats_food(self):
        head = self.snake.get_head()

        for piece in self.food:
            if piece.pos == head:
                return piece

        return None