from p5 import *

import game

speed = 0.1
step = 40
game = game.Game(8, 8)


def setup():
    # Set size of the canvas
    size(step * (game.grid.width + 1), step * (game.grid.height + 1))


def draw():
    time.sleep(speed)
    game.update()
    led_grid = create_grid(game.grid.width, game.grid.height, game.snake, game.apples)
    background(225)
    no_stroke()

    # Draw the grid of leds
    for led_row in led_grid:
        for led in led_row:
            fill(led.col)
            circle(step * (led.x + 1), step * (led.y + 1), 15)


def create_grid(width, height, snake, apples):
    grid = []
    for i in range(0, height):
        grid.append([])
        for j in range(0, width):
            grid[i].append(Led(j, i, Color(0, 0, 0)))

    if snake is not None:
        for element in snake.elements:
            if element.x < width and element.y < height:
                grid[element.y][element.x].set_color(Color(0, 255, 0))

    if apples:
        apple = apples[0]
        grid[apple.pos.x][apple.pos.y].set_color(Color(255, 0, 0))

    return grid

def key_pressed():
    game.process_input(key)

class Led:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.col = c

    def set_color(self, c):
        self.col = c


if __name__ == '__main__':
    run()

