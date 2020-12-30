class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
