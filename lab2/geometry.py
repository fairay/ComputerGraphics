from vals import *
from math import *


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def adp_xy(self):
        return (self.x) / (x_max - x_min) * canvas_x, \
               (-self.y) / (y_max - y_min) * canvas_y
        # return (self.x - x_min) / (x_max - x_min) * canvas_x, \
        #       (y_max - self.y) / (y_max - y_min) * canvas_y

    def move_by(self, p):
        self.x += p.x
        self.y += p.y

    def rotate_by(self, p, a):
        x1 = p.x + (self.x - p.x)*cos(radians(a)) + (self.y - p.y)*sin(radians(a))
        y1 = p.y - (self.x - p.x)*sin(radians(a)) + (self.y - p.y)*cos(radians(a))
        self.x, self.y = x1, y1

    def scale_by(self, p, kx, ky):
        self.x = kx * self.x + (1 - kx) * p.x
        self.y = ky * self.y + (1 - ky) * p.y



## Параметры
# Астроиды
zero_R = 5
bx_zero = zero_R
by_zero = zero_R
start_angle_zero = 0
center_zero = Point(0, 0)

# Прямоушльника
rect_zero = [Point(0, zero_R), Point(zero_R, 0),
             Point(0, -zero_R), Point(-zero_R, 0)]



