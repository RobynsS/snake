from enum import Enum
import canvas


class Snake:
    def __init__(self, pos, direction):
        self.elements = [pos]
        self.direction = direction

    def get_snake(self):
        return self.elements

    def get_head(self):
        length = len(self.elements)
        return self.elements[length - 1]

    def set_head(self, head):
        length = len(self.elements)
        self.elements[length - 1] = head

    def grow(self):
        # Add new head to snake
        old_head = self.get_head()
        new_head = None
        if self.direction == Direction.RIGHT:
            new_head = canvas.Point(old_head.x + 1, old_head.y)
        elif self.direction == Direction.DOWN:
            new_head = canvas.Point(old_head.x, old_head.y + 1)
        elif self.direction == Direction.LEFT:
            new_head = canvas.Point(old_head.x - 1, old_head.y)
        elif self.direction == Direction.UP:
            new_head = canvas.Point(old_head.x, old_head.y - 1)

        self.elements.append(new_head)

    def move(self):
        self.grow()

        # Remove tail
        self.elements.pop(0)

    def set_direction(self, new_direction):
        if new_direction != self.direction.opposite():
            self.direction = new_direction


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

    def opposite(self):
        if self.value == 1:
            return Direction.LEFT
        elif self.value == 2:
            return Direction.UP
        elif self.value == 3:
            return Direction.RIGHT
        elif self.value == 4:
            return Direction.DOWN
        else:
            return None


class Apple:
    def __init__(self, pos):
        self.pos = pos
