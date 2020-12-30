from p5 import *

import canvas
import objects

grid_height = 8
grid_width = 8
step = 40
snake = objects.Snake(canvas.Point(1, 0))
apple = objects.Apple(canvas.Point(2, 3))


def setup():
    # Set size of the canvas
    size(step * (grid_width + 1), step * (grid_height + 1))


def draw():
    snake.move()
    led_grid = draw_grid(grid_width, grid_height, snake, apple)
    background(225)
    no_stroke()

    # Draw the grid of leds
    for led_row in led_grid:
        for led in led_row:
            fill(led.col)
            circle(step * (led.x + 1), step * (led.y + 1), 15)


def draw_grid(width, height, snake, apple):
    grid = []
    for i in range(0, height):
        grid.append([])
        for j in range(0, width):
            grid[i].append(Led(j, i, Color(0, 0, 0)))

    if snake is not None:
        for element in snake.elements:
            grid[element.y][element.x].set_color(Color(0, 255, 0))

    if apple is not None:
        grid[apple.pos.x][apple.pos.y].set_color(Color(255, 0, 0))

    return grid


class Led:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.col = c

    def set_color(self, c):
        self.col = c


if __name__ == '__main__':
    run()

