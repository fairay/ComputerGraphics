from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor, QImage
from math import *

# EPS = 10e-3
EPS = 1


class Stack(object):
    point_list = list()

    def pop(self):
        return self.point_list.pop()

    def push(self, x, y):
        self.point_list.append((x, y))

    def is_not_empty(self):
        return len(self.point_list) != 0


class Segment(object):
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    def __init__(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2


class MyScene(QtWidgets.QGraphicsScene):
    segment_arr = []
    first_point = None
    link_dist = 10

    rect1 = None
    rect2 = None
    rect_obj = None
    x_left, x_right = 0, 0
    y_up, y_low = 0, 0

    edge_color = Qt.red
    edge_pen = QPen(edge_color)
    edge_pen.setWidth(1)

    cut_color = Qt.white
    cut_pen = QPen(cut_color)

    result_color = Qt.yellow
    result_pen = QPen(result_color)

    inv_brush = QBrush(QColor(Qt.black))

    image = QImage()
    image_size = (0, 0)
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0

    def setup(self, bg_color, x_size, y_size):
        self.image_size = (x_size, y_size)
        self.max_x, self.max_y = x_size - 1, y_size - 1

        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))

        inv_color = QColor(bg_color)
        inv_color.setAlphaF(0)
        self.inv_brush = QBrush(inv_color)

        self.clear_image()
        # По заданию нужно было показать заполнение на кривой
        # Для отрисовки эллипса просто разкоментировать строку)
        # self.drawe_canonical(300, 300, 200, 140)
        self.update_image()

    def clear(self, clear_image=True):
        super().clear()
        if clear_image:
            self.segment_arr = []
            self.first_point = None

            self.rect1, self.rect2 = None, None
            self.rect_obj = None
            self.clear_image()

    # Clear the QImage (delete all pixels)
    def clear_image(self):
        self.image = QImage(*self.image_size, QImage.Format_RGB32)

    # Set the brush's colors
    def set_edge_color(self, color):
        self.edge_color = color
        self.edge_pen.setColor(QColor(color))

    def set_cut_color(self, color):
        self.cut_color = color
        self.cut_pen.setColor(QColor(color))

    # Input edges function
    def input_point(self, point, is_orto, color):
        if self.first_point is None:
            self.first_point = point
            self.set_edge_color(color)
            return

        if is_orto:
            dx = point[0] - self.first_point[0]
            dy = point[1] - self.first_point[1]
            # Горизонтальная линия
            if abs(dx) > abs(dy):
                point[1] = self.first_point[1]
            else:
                point[0] = self.first_point[0]

        self.add_edge(self.first_point, point)
        self.first_point = None

    def is_closed(self, point):
        x_into = abs(self.first_point[0] - point[0]) < self.link_dist
        y_into = abs(self.first_point[1] - point[1]) < self.link_dist
        return x_into and y_into

    def add_edge(self, p1, p2):
        if p1 == p2:
            return
        # self.draw_DDP(p1, p2)
        # self.update_image()
        if len(self.segment_arr) < 10:
            self.addLine(*p1, *p2, self.edge_pen)
            # self.segment_arr.append(Segment(p1, p2))
            self.segment_arr.append((p1, p2))

    def add_cut_point(self, point):
        if self.rect1 is None:
            self.rect1 = point
        elif self.rect2 is None:
            self.rect2 = point

            self.x_left = min(self.rect2[0], self.rect1[0])
            self.x_right = max(self.rect2[0], self.rect1[0])
            self.y_low = min(self.rect2[1], self.rect1[1])
            self.y_up = max(self.rect2[1], self.rect1[1])

            dx = self.x_right - self.x_left
            dy = self.y_up - self.y_low
            self.rect_obj = self.addRect(self.x_left, self.y_low, dx, dy,
                                         self.cut_pen, self.inv_brush)
        else:
            self.removeItem(self.rect_obj)
            self.rect1 = point
            self.rect2 = None

    #
    # Middle point cut algorithm
    #
    def mid_point_cut(self):
        for seg in self.segment_arr:
            p1, p2 = seg
            i = 0
            draw_flag = True
            while True:
                t1 = self.point_code(p1)
                t2 = self.point_code(p2)

                sum1 = self.code_sum(t1)
                sum2 = self.code_sum(t2)
                # Отрезок полностью видим
                if sum1 == 0 and sum2 == 0:
                    break
                # Отрезок полностью невидим
                if self.code_and(t1, t2):
                    draw_flag = False
                    break

                temp = p1
                if i == 2:
                    # if self.code_and(t1, t2):
                        # draw_flag = False
                    draw_flag = not self.code_and(t1, t2)
                    break
                """
                while sum2 and self.distance(p1, p2) > EPS:
                    pm = self.mid_point(p1, p2)
                    temp = p1
                    p1 = pm

                    t1 = self.point_code(p1)

                    if self.code_and(t1, t2):
                        p1 = temp
                        p2 = pm
                """
                while sum2 and self.distance(p1, p2) > EPS:
                    pm = self.mid_point(p1, p2)
                    t1 = self.point_code(pm)
                    if self.code_and(t1, t2):   p2 = pm
                    else:                       p1 = pm
                p1 = p2
                p2 = temp
                i += 1

            if draw_flag:
                self.draw_line(p1, p2)

    def point_code(self, point):
        t = [0] * 4
        if point[0] < self.x_left:  t[3] = 1
        if point[0] > self.x_right: t[2] = 1
        if point[1] < self.y_low:   t[1] = 1
        if point[1] > self.y_up:    t[0] = 1
        return t

    def code_sum(self, t_code):
        return sum(t_code)
    def code_and(self, t1, t2):
        res = 0
        for i in range(4):
            if t1[i] and t2[i]:
                res += 1
        return res
    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def mid_point(self, p1, p2):
        x = (p1[0] + p2[0]) / 2
        y = (p1[1] + p2[1]) / 2
        return [x, y]

    # Drawing pixels
    def draw_edge_pixel(self, x, y):
        self.image.setPixelColor(x, y, self.edge_color)
    def draw_fill_pixel(self, x, y):
        self.image.setPixelColor(x, y, self.cut_color)

    # Scanning pixels
    def is_border_pixel(self, x, y):
        return self.image.pixelColor(x, y) == self.edge_color
    def is_fill_pixel(self, x, y):
        return self.image.pixelColor(x, y) == self.cut_color

    # Figures drawing
    def draw_line(self, p1, p2):
        self.addLine(*p1, *p2, self.result_pen)

    def draw_DDP(self, p1, p2):
        x, y = p1
        dx = p2[0] - x
        dy = p2[1] - y

        dl = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        if dl == 0:
            self.draw_edge_pixel(round(x), round(y))
            return

        dx /= dl
        dy /= dl
        for i in range(int(dl)):
            self.draw_edge_pixel(round(x), round(y))
            x += dx
            y += dy
        self.draw_edge_pixel(round(x), round(y))

    def drawe_canonical(self, x0, y0, a, b):
        x = 0
        a2 = a*a
        b2 = b*b
        max_x = round(sqrt(a2 / (b2 / a2 + 1)))
        while x <= max_x:
            y = round(b * sqrt(1 - x*x / a2))
            self.draw_edge_pixel(x + x0, y + y0)
            self.draw_edge_pixel(x + x0, -y + y0)
            self.draw_edge_pixel(-x + x0, y + y0)
            self.draw_edge_pixel(-x + x0, -y + y0)
            x += 1

        y = 0
        max_y = round(sqrt(b2 / (a2 / b2 + 1)))
        while y <= max_y:
            x = round(a * sqrt(1 - y*y / b2))
            self.draw_edge_pixel(x + x0, y + y0)
            self.draw_edge_pixel(x + x0, -y + y0)
            self.draw_edge_pixel(-x + x0, y + y0)
            self.draw_edge_pixel(-x + x0, -y + y0)
            y += 1

    def make_delay(self, delay):
        QtWidgets.QApplication.processEvents()
        QThread.msleep(delay)

    def update_image(self):
        self.clear(False)
        pixmap = QtGui.QPixmap()
        pixmap = pixmap.fromImage(self.image)
        self.addPixmap(pixmap)
