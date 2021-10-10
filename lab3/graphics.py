from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QPen, QColor
from copy import copy
from math import *

EPS = 10e-3


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return int(self.x - other.x), int(self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __copy__(self):
        return Point(self.x, self.y)


class MyScene(QtWidgets.QGraphicsScene):
    pen = QPen(Qt.black)
    pen.setWidth(1)
    color = QColor(Qt.black)

    def setup(self, bg_color, draw=True, x=100, y=100):
        self.x_off = x
        self.y_off = y
        self.is_draw = draw
        self.setSceneRect(-10, -10, 10, 10)
        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))
        self.clear()

    def set_color(self, color=None):
        if color is None:
            color = self.bg_color
        self.color = QColor(color)
        self.pen.setColor(color)

    def draw_DDP(self, st_p, end_p):
        x = int(st_p.x)
        y = int(st_p.y)
        dx, dy = end_p - st_p

        dl = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        if dl == 0:
            self.draw_pixel(end_p)
            return

        dx /= dl
        dy /= dl
        for i in range(int(dl)):
            self.draw_pixel_xy(x, y)
            x += dx
            y += dy
        self.draw_pixel_xy(x, y)
        if round(x) != end_p.x or round(y) != end_p.y:
            self.draw_error_pixel(end_p.x, end_p.y)

    def draw_default(self, st_p, end_p):
        self.addLine(st_p.x - self.x_off, -st_p.y + self.y_off,
                     end_p.x - self.x_off, -end_p.y + self.y_off,
                     self.pen)

    def draw_Bres_int(self, st_p, end_p):
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = int(copysign(1, dx)), int(copysign(1, dy))
        dx, dy = dx * sx, dy * sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            self.draw_pixel(end_p)
            return

        dx2 = dx*2
        dy2 = dy*2

        e = dy2 - dx
        for i in range(dx):
            self.draw_pixel_int(x, y)
            if e >= 0:
                if swap:    x += sx
                else:       y += sy
                e -= dx2
            if swap:    y += sy
            else:       x += sx
            e += dy2
        self.draw_pixel_int(x, y)
        if round(x) != end_p.x or round(y) != end_p.y:
            self.draw_error_pixel(end_p.x, end_p.y)

    def draw_Bres_float(self, st_p, end_p):
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = copysign(1, dx), copysign(1, dy)
        dx, dy = dx*sx, dy*sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            self.draw_pixel(end_p)
            return

        m = dy/dx
        e = m - 0.5

        for i in range(int(dx)):
            self.draw_pixel_xy(x, y)
            if e >= 0:
                if swap:    x += sx
                else:       y += sy
                e -= 1
            if swap:    y += sy
            else:       x += sx
            e += m
        self.draw_pixel_xy(x, y)

        if round(x) != end_p.x or round(y) != end_p.y:
            self.draw_error_pixel(end_p.x, end_p.y)


    def draw_Bres_smooth(self, st_p, end_p):
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = copysign(1, dx), copysign(1, dy)
        dx, dy = dx*sx, dy*sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            self.draw_pixel(end_p)
            return

        m = dy/dx
        e = 0.5
        w = 1 - m

        self.draw_pixel_xy(x, y, e)
        for i in range(int(dx)):
            if e < w:
                if swap:    y += sy
                else:       x += sx
                e += m
            else:
                y += sy
                x += sx
                e -= w
            self.draw_pixel_xy(x, y, e)

        if round(x) != end_p.x or round(y) != end_p.y:
            self.draw_error_pixel(end_p.x, end_p.y)

    def draw_Wu(self, st_p, end_p):
        dx, dy = end_p - st_p
        sx, sy = copysign(1, dx), copysign(1, dy)
        dx, dy = dx * sx, dy * sy

        x = st_p.x
        y = st_p.y

        if dy > dx:
            dx, dy = dy, dx
            swap = True
        else:
            swap = False
        m = dy/dx

        self.draw_pixel(st_p)

        if swap:
            y += sy
            x += sx * m
        else:
            x += sx
            y += sy * m

        for i in range(int(dx)):
            if swap:
                self.draw_pixel_xy(int(x), y, 1 - (x % 1))
                self.draw_pixel_xy(int(x) + 1, y, (x % 1))
                y += sy
                x += sx*m
            else:
                self.draw_pixel_xy(x, int(y), 1 - (y % 1))
                self.draw_pixel_xy(x, int(y) + 1, (y % 1))
                x += sx
                y += sy*m

        if round(x) != end_p.x or round(y) != end_p.y:
            self.draw_error_pixel(end_p.x, end_p.y)


    #
    def show_Time(self, time_arr):
        stat_pen = QPen(Qt.yellow)
        stat_brush = QBrush(Qt.red)
        self.clear()
        max_t = max(time_arr)

        for i in range(len(time_arr)):
            self.addRect(i*90 - 250, -(time_arr[i]/max_t) * 200 + 100,
                         70, (time_arr[i]/max_t) * 200,
                         stat_pen, stat_brush)

    #
    def draw_pixel(self, point, intensity=1):
        if not self.is_draw:
            return
        self.color.setAlphaF(intensity)
        self.pen.setColor(self.color)
        self.addLine(round(point.x) - self.x_off, -round(point.y) + self.y_off,
                     round(point.x) - self.x_off, -round(point.y) + self.y_off,
                     self.pen)

    def draw_pixel_xy(self, x, y, intensity=1):
        if not self.is_draw:
            return
        self.color.setAlphaF(intensity)
        self.pen.setColor(self.color)
        self.addLine(round(x) - self.x_off, -round(y) + self.y_off,
                     round(x) - self.x_off, -round(y) + self.y_off,
                     self.pen)

    def draw_error_pixel(self, x, y):
        stat_pen = QPen(Qt.darkMagenta)
        self.addLine(round(x) - self.x_off, -round(y) + self.y_off,
                     round(x) - self.x_off, -round(y) + self.y_off,
                     stat_pen)

    def draw_pixel_int(self, x, y):
        self.addLine(x - self.x_off, -y + self.y_off,
                     x - self.x_off, -y + self.y_off,
                     self.pen)


class StepAnalysis(object):
    def DDA(self, st_p, end_p):
        steps = 0
        x = int(st_p.x)
        y = int(st_p.y)
        dx, dy = end_p - st_p

        dl = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        if dl == 0:
            return steps

        dx /= dl
        dy /= dl

        for i in range(int(dl)):
            if (int(x) != int(x + dx)) and (int(y) != int(y + dy)):
                steps += 1
            x += dx
            y += dy
        return steps

    def Bres_int(self, st_p, end_p):
        steps = 0
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = int(copysign(1, dx)), int(copysign(1, dy))
        dx, dy = dx * sx, dy * sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            return steps

        dx2 = dx * 2
        dy2 = dy * 2

        e = dy2 - dx
        for i in range(dx):
            if e >= 0:
                if swap:    x += sx
                else:       y += sy
                e -= dx2
                steps += 1

            if swap:    y += sy
            else:       x += sx
            e += dy2
        return steps

    def Bres_float(self, st_p, end_p):
        steps = 0
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = copysign(1, dx), copysign(1, dy)
        dx, dy = dx*sx, dy*sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            return steps

        m = dy/dx
        e = m - 0.5

        for i in range(int(dx)):
            if e >= 0:
                if swap:    x += sx
                else:       y += sy
                e -= 1
                steps += 1
            if swap:    y += sy
            else:       x += sx
            e += m
        return steps

class MaxLenAnalysis(object):
    def DDA(self, st_p, end_p):
        max_len = 0
        temp_len = 0
        x = int(st_p.x)
        y = int(st_p.y)
        dx, dy = end_p - st_p

        dl = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        if dl == 0:
            return max_len

        dx /= dl
        dy /= dl

        for i in range(int(dl)):
            if (int(x) != int(x + dx)) and (int(y) != int(y + dy)):
                max_len = max(max_len, temp_len)
                temp_len = 1
            else:
                temp_len += 1

            x += dx
            y += dy
        max_len = max(max_len, temp_len)
        return max_len

    def Bres_int(self, st_p, end_p):
        max_len = 0
        temp_len = 0
        x = int(st_p.x)
        y = int(st_p.y)

        dx, dy = end_p - st_p
        sx, sy = int(copysign(1, dx)), int(copysign(1, dy))
        dx, dy = dx * sx, dy * sy

        if dx > dy:
            swap = 0
        else:
            swap = 1
            dx, dy = dy, dx

        if dx == 0:
            return max_len

        dx2 = dx * 2
        dy2 = dy * 2

        e = dy2 - dx
        for i in range(dx):
            if e >= 0:
                if swap:    x += sx
                else:       y += sy
                e -= dx2
                max_len = max(max_len, temp_len)
                temp_len = 0

            if swap:    y += sy
            else:       x += sx
            e += dy2
            temp_len += 1
        max_len = max(max_len, temp_len)
        return max_len
