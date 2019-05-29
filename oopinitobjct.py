import math

class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(6, 9)

    def calculate_distance(self, other_point):
        return math.sqrt(
             (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2)
point = Point(5, 3)
print(point.x, point.y)
