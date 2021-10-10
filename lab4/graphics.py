from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QPen, QColor
from math import *

EPS = 10e-3


class MyScene(QtWidgets.QGraphicsScene):
    pen = QPen(Qt.black)
    pen.setWidth(1)
    brush = QBrush(Qt.black)
    color = QColor(Qt.black)

    def setup(self, bg_color, draw=True, x=100, y=100):
        self.x_off = x
        self.y_off = y
        self.is_draw = draw
        self.setSceneRect(-10, -10, 10, 10)
        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))
        self.init_brush()
        self.clear()

    def get_draw_circle(self):
        return (self.drawc_canonical,
                self.drawc_parametric,
                self.drawc_bres,
                self.drawc_mid_point,
                self.drawc_default)

    def get_draw_ellipse(self):
        return (self.drawe_canonical,
                self.drawe_parametric,
                self.drawe_bres,
                self.drawe_mid_point,
                self.drawe_default)

    def init_brush(self):
        color = QColor(Qt.black)
        color.setAlphaF(0)
        self.brush.setColor(color)
        pass

    def set_color(self, color=None):
        if color is None:
            color = self.bg_color
        self.color = QColor(color)
        self.pen.setColor(color)

    # Каноническое уравнение
    def drawc_canonical(self, x0, y0, r):
        r2 = r*r
        x = 0
        y = r
        while x <= y:
            y = round(sqrt(r2 - x*x))
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            self.draw_pixel(y + x0, x + y0)
            self.draw_pixel(y + x0, -x + y0)
            self.draw_pixel(-y + x0, x + y0)
            self.draw_pixel(-y + x0, -x + y0)
            x += 1

    """
        y = 0
        while y < r * 1/sqrt(2):
            x = sqrt(r*r - y*y)
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)
            y += 1
    """
    def drawe_canonical(self, x0, y0, a, b):
        x = 0
        a2 = a*a
        b2 = b*b
        max_x = round(sqrt(a2 / (b2 / a2 + 1)))
        while x <= max_x:
            y = round(b * sqrt(1 - x*x / a2))
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)
            x += 1

        y = 0
        max_y = round(sqrt(b2 / (a2 / b2 + 1)))
        while y <= max_y:
            x = round(a * sqrt(1 - y*y / b2))
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)
            y += 1

    # Параметрическое уравнение
    def drawc_parametric(self, x0, y0, r):
        k = 1/r

        deg = 0
        while deg <= pi/4 + EPS:
            x = round(r * cos(deg))
            y = round(r * sin(deg))

            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            self.draw_pixel(y + x0, x + y0)
            self.draw_pixel(y + x0, -x + y0)
            self.draw_pixel(-y + x0, x + y0)
            self.draw_pixel(-y + x0, -x + y0)

            deg += k

    def drawe_parametric(self, x0, y0, a, b):
        k = min(a / (b*b), b / (a*a))

        deg = 0
        while deg <= pi/2 + EPS:
            x = round(a * cos(deg))
            y = round(b * sin(deg))

            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            deg += k

    # Алгоритм Брезенхема
    def drawc_bres(self, x0, y0, r):
        x = 0
        y = r
        d = 2 * (1 - r)
        while y >= x:
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            self.draw_pixel(y + x0, x + y0)
            self.draw_pixel(y + x0, -x + y0)
            self.draw_pixel(-y + x0, x + y0)
            self.draw_pixel(-y + x0, -x + y0)

            if d < 0:
                e = 2*(d + y) - 1
                if e <= 0:
                    x += 1
                    d += 2*x + 1
                    continue
            elif d > 0:
                e = 2*(d - x) - 1
                if e > 0:
                    y -= 1
                    d += -2*y + 1
                    continue
            x += 1
            y -= 1
            d += 2 * (x - y + 1)

    def drawe_bres(self, x0, y0, a, b):
        a2 = a*a
        b2 = b*b

        x = 0
        y = b
        d = 1/a2 + (1 - 2*b)/b2
        while y >= 0:
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            if d < 0:
                e = 2*d + (2*y - 1)/b2
                if e <= 0:
                    x += 1
                    d += (2*x + 1)/a2
                    continue
            elif d > 0:
                e = 2*d - (2*x + 1)/a2
                if e > 0:
                    y -= 1
                    d += (-2*y + 1)/b2
                    continue
            # d == 0 or e
            x += 1
            y -= 1
            d += (2*x + 1)/a2 + (-2*y + 1)/b2

    # Алгортим средней точки
    def drawc_mid_point(self, x0, y0, r):
        x = 0
        y = r

        f_tf = 1.25 - r
        dy = 2*y
        dx = 1

        while y >= x:
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            self.draw_pixel(y + x0, x + y0)
            self.draw_pixel(y + x0, -x + y0)
            self.draw_pixel(-y + x0, x + y0)
            self.draw_pixel(-y + x0, -x + y0)

            x += 1
            if f_tf >= 0:
                y -= 1
                dy -= 2
                f_tf -= dy      # 2*y

            dx += 2
            f_tf += dx          # 2*x + 1

    def drawe_mid_point(self, x0, y0, a, b):
        a2 = a*a
        b2 = b*b
        ad = 2*a2
        bd = 2*b2

        x = 0
        y = b

        # Интервал 1
        f_tf = b2 - a2*b + a2/4
        dy = y*ad
        dx = b2
        while a2*y >= b2*x:
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            x += 1
            if f_tf >= 0:
                y -= 1
                dy -= ad
                f_tf -= dy  # 2*y*a2
            dx += bd
            f_tf += dx      # b2 * (2*x + 1)

        # Интервал 2
        f_tf -= b2*(x+0.75) + a2*(y-0.75)
        dx = x*bd
        dy = a2 * (2*y - 1)
        while y >= 0:
            self.draw_pixel(x + x0, y + y0)
            self.draw_pixel(x + x0, -y + y0)
            self.draw_pixel(-x + x0, y + y0)
            self.draw_pixel(-x + x0, -y + y0)

            y -= 1
            if f_tf <= 0:
                x += 1
                dx += bd
                f_tf += dx  # 2*x*b2
            dy -= ad
            f_tf -= dy      # a2 * (2*y - 1)

    # Встроеный метод
    def drawc_default(self, x, y, r):
        self.addEllipse(x - r - self.x_off,
                        -y - r + self.y_off,
                        2*r, 2*r,
                        self.pen, self.brush)

    def drawe_default(self, x, y, a, b):
        self.addEllipse(x - a - self.x_off,
                        -y - b + self.y_off,
                        2 * a, 2 * b,
                        self.pen, self.brush)

    """
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
    """
    """
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
    """

    def draw_error_pixel(self, x, y):
        stat_pen = QPen(Qt.darkMagenta)
        self.addLine(round(x) - self.x_off, -round(y) + self.y_off,
                     round(x) - self.x_off, -round(y) + self.y_off,
                     stat_pen)

    def draw_pixel(self, x, y):
        self.addLine(x - self.x_off, -y + self.y_off,
                     x - self.x_off, -y + self.y_off,
                     self.pen)

    def draw_line(self, x1, y1, x2, y2):
        self.addLine(x1 - self.x_off, -y1 + self.y_off,
                     x2 - self.x_off, -y2 + self.y_off,
                     self.pen)


"""     
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
"""
