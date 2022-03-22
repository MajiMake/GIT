import math


class Vec2d:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '({},{})'.format(self.a, self.b)

    def len(self) -> float:
        return math.sqrt(self.a ** 2 + self.b ** 2)


    def __add__(self, other):
        return Vec2d(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vec2d(self.a - other.a, self.b - other.b)

    def scale(self, scalar_value):
        return Vec2d(self.a * scalar_value, self.b * scalar_value)

    def dot(self, other):
        return self.a * other.a + self.b * other.b

    def rot(self, angle):
        rad_angle = math.radians(angle)
        x = self.a * math.cos(rad_angle) - self.b * math.sin(rad_angle)
        y = self.a * math.cos(rad_angle) + self.b * math.sin(rad_angle)
        return Vec2d(round(x, 2), round(y, 2))
        pass

    def normalize(self):
       return Vec2d(self.a / self.len(), self.b / self.len())
