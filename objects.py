from enum import Enum
import canvas


class Snake:
    def __init__(self, pos):
        self.elements = [pos]
        self.direction = Direction.RIGHT

    def get_snake(self):
        return self.elements

    def get_head(self):
        length = len(self.elements)
        return self.elements[length - 1]

    def move(self):

        # Add new head to snake
        old_head = self.get_head()
        new_head = None
        if self.direction == Direction.RIGHT:
            new_head = canvas.Point(old_head.x + 1, old_head.y)
        elif self.direction == Direction.DOWN:
            new_head = canvas.Point(old_head.x, old_head.y - 1)
        elif self.direction == Direction.LEFT:
            new_head = canvas.Point(old_head.x - 1, old_head.y)
        elif self.direction == Direction.UP:
            new_head = canvas.Point(old_head.x, old_head.y + 1)

        self.elements.append(new_head)

        # Remove tail
        self.elements.pop(0)

        print(self.elements)


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


class Apple:
    def __init__(self, pos):
        self.pos = pos