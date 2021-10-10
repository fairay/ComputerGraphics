from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor, QImage
from math import *


def frange(a, b, step=1):
    arr = []
    if step > 0 and a < b:
        while a <= b + 0.001:
            arr.append(a)
            a += step
    elif step < 0 and a > b:
        while a >= b - 0.001:
            arr.append(a)
            a += step
    return arr


class MyScene(QtWidgets.QGraphicsScene):
    link_dist = 10

    min_hor = None
    max_hor = None
    angles = [0, 0, 0]

    x_res = 400
    y_res = 400

    edge_color = Qt.red
    edge_pen = QPen(edge_color)

    inv_brush = QBrush(QColor(Qt.black))

    def setup(self, bg_color, res):
        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))

        self.x_res, self.y_res = res

        inv_color = QColor(bg_color)
        inv_color.setAlphaF(0)
        self.inv_brush = QBrush(inv_color)

    def clear(self, clear_image=True):
        super().clear()

    # Set the brush's colors
    def set_edge_color(self, color):
        self.edge_color = color
        self.edge_pen.setColor(QColor(color))

    def is_closed(self, first_point, point):
        x_into = abs(first_point[0] - point[0]) < self.link_dist
        y_into = abs(first_point[1] - point[1]) < self.link_dist
        return x_into and y_into

    # Figures drawing
    def draw_line(self, p1, p2):
        self.addLine(*p1, *p2, self.edge_pen)

    #
    # Surface draw algorithm
    #
    def find_minmax(self, func, x_par, z_par):
        x0_min, x0_max = 1e20, -1e20
        y_min, y_max = 1e20, -1e20
        x_min, x_max, x_step = x_par
        z_min, z_max, z_step = z_par

        for z in frange(z_min, z_max + 1, z_step):
            for x in frange(x_min, x_max, x_step):
                y = func(x, z)
                x0, y, z0 = self.rotate((x, y, z))

                y_min = min(y, y_min)
                y_max = max(y, y_max)

                x0_min = min(x0, x0_min)
                x0_max = max(x0, x0_max)

        d = (x0_max - x0_min) - (y_max - y_min)
        if d > 0:
            y_min -= d/2
            y_max += d/2
        else:
            d = -d
            x0_min -= d/2
            x0_max += d/2
        return (x0_min, x0_max), (y_min, y_max)

    def transform(self, x0, y0, z0, x_par, y_par=(-10, 1000)):
        x0, y0, z0 = self.rotate((x0, y0, z0))

        x = (x0 - x_par[0]) / (x_par[1] - x_par[0])
        x = 10 + x * (self.x_res - 20)

        y = (y0 - y_par[0]) / (y_par[1] - y_par[0])
        y = 10 + y * (self.y_res - 20)
        y = self.y_res - y

        return int(x), int(y)

    def transform_x_par(self, func, x_par, z_par):
        print("SEARCHING FOR X MIN MAX", "!"*100)
        y = func(x_par[0], z_par[0])
        x0, y, z0 = self.rotate((x_par[0], y, z_par[0]))

        y = func(x_par[1], z_par[0])
        x1, y, z = self.rotate((x_par[1], y, z_par[0]))

        y = func(x_par[0], z_par[1])
        x2, y, z = self.rotate((x_par[0], y, z_par[1]))

        y = func(x_par[1], z_par[1])
        x3, y, z3 = self.rotate((x_par[1], y, z_par[1]))
        print("Edges", x0, x1, x2, x3)
        return (min(x0, x1, x2, x3), max(x0, x1, x2, x3))

    def rotate(self, p):
        p = self.rotate_ox(p)
        p = self.rotate_oy(p)
        p = self.rotate_oz(p)
        return p
    def rotate_ox(self, p):
        alpha = self.angles[0]
        y = p[1] * cos(alpha) + p[2] * sin(alpha)
        z = -p[1] * sin(alpha) + p[2] * cos(alpha)
        return p[0], y, z
    def rotate_oy(self, p):
        alpha = self.angles[1]
        x = p[0] * cos(alpha) - p[2] * sin(alpha)
        z = p[0] * sin(alpha) + p[2] * cos(alpha)
        return x, p[1], z
    def rotate_oz(self, p):
        alpha = self.angles[2]
        x = p[0] * cos(alpha) + p[1] * sin(alpha)
        y = -p[0] * sin(alpha) + p[1] * cos(alpha)
        return x, y, p[2]

    def draw_surface(self, func, angles, x_par, z_par):
        self.angles = angles
        x_minmax, y_minmax = self.find_minmax(func, x_par, z_par)

        x_min, x_max, x_step = x_par
        z_min, z_max, z_step = z_par

        self.min_hor = [self.y_res] * self.x_res
        self.max_hor = [0] * self.x_res
        x_l, y_l, x_r, y_r = [-1] * 4

        for z in frange(z_max, z_min, -z_step):
            x_pre = x_min
            y_pre = func(x_min, z)
            x_pre, y_pre = self.transform(x_pre, y_pre, z, x_minmax, y_minmax)

            x_l, y_l = self.edge_process(x_pre, y_pre, x_l, y_l)
            pre_flag = self.is_visible(x_pre, y_pre)

            for x0 in frange(x_min, x_max, x_step):
                y = func(x0, z)
                x, y = self.transform(x0, y, z, x_minmax, y_minmax)

                temp_flag = self.is_visible(x, y)
                if pre_flag == temp_flag:
                    if temp_flag != 0:
                        self.draw_line((x_pre, y_pre), (x, y))
                        self.horizon(x_pre, y_pre, x, y)
                else:
                    if temp_flag == 0:
                        if pre_flag == 1:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.max_hor)
                        else:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.min_hor)
                        self.draw_line((x_pre, y_pre), cross_p)
                        self.horizon(x_pre, y_pre, *cross_p)

                    elif temp_flag == 1:
                        if pre_flag == 0:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.max_hor)
                            self.draw_line(cross_p, (x, y))
                            self.horizon(*cross_p, x, y)
                        else:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.min_hor)
                            self.draw_line((x_pre, y_pre), cross_p)
                            self.horizon(x_pre, y_pre, *cross_p)

                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.max_hor)
                            self.draw_line(cross_p, (x, y))
                            self.horizon(*cross_p, x, y)
                    else:
                        if pre_flag == 0:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.min_hor)
                            self.draw_line((x, y), cross_p)
                            self.horizon(*cross_p, x, y)
                        else:
                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.max_hor)
                            self.draw_line((x_pre, y_pre), cross_p)
                            self.horizon(x_pre, y_pre, *cross_p)

                            cross_p = self.edge_cross(x_pre, y_pre, x, y, self.min_hor)
                            self.draw_line(cross_p, (x, y))
                            self.horizon(*cross_p, x, y)
                pre_flag = temp_flag
                x_pre = x
                y_pre = y

            x_r, y_r = self.edge_process(x, y, x_r, y_r)

    def edge_process(self, x, y, x_edge, y_edge):
        if x_edge != -1:
            self.horizon(x_edge, y_edge, x, y)
            self.draw_line((x_edge, y_edge), (x, y))
        return x, y

    def horizon(self, x1, y1, x2, y2):
        x1, x2 = int(x1), int(x2)
        if x2 == x1:
            self.max_hor[x2] = max(self.max_hor[x2], y2)
            self.min_hor[x2] = min(self.min_hor[x2], y2)
        else:
            k = (y2 - y1)/(x2 - x1)
            for x in range(x1, x2):
                y = int(k * (x - x1) + y1)
                self.max_hor[x] = max(self.max_hor[x], y)
                self.min_hor[x] = min(self.min_hor[x], y)

    def is_visible(self, x, y):
        x = int(x)
        if y < self.max_hor[x] and y > self.min_hor[x]: return 0
        elif y >= self.max_hor[x]: return 1
        else:                      return -1

    def edge_cross(self, x1, y1, x2, y2, hor_arr):
        x1, x2 = int(x1), int(x2)
        if x1 == x2:
            xi = x2
            yi = hor_arr[x2]
        elif y2 - y1 == hor_arr[x2] - hor_arr[x1]:
            xi = x1
            yi = hor_arr[x1]
        else:
            dx = x2 - x1
            dy = y2 - y1
            dh = hor_arr[x2] - hor_arr[x1]
            k = dy / dx

            xi = x1 - round(dx * (y1 - hor_arr[x1]) / (dy - dh))
            yi = round(y1 + k*(xi - x1))
            return (xi, yi)

            ysign = sign(y1 + k - hor_arr[x1 + 1])
            csign = ysign

            yi = y1
            xi = x1
            while ysign == csign and xi < x2: # and xi < self.x_res - 1:
                yi += k
                xi += 1
                csign = sign(yi - hor_arr[xi])
            # if xi == x2: print("NOT GET IT!")
            if fabs(yi - k - hor_arr[xi-1]) <= fabs(yi - hor_arr[xi-1]):
                yi -= k
                xi -= 1
        return (xi, yi)


def sign(x):
    if x == 0: return 0
    elif x < 0: return -1
    else: return 1
