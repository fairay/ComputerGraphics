from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor, QImage
from math import *

EPS = 10e-3


class Stack(object):
    point_list = list()

    def pop(self):
        return self.point_list.pop()

    def push(self, x, y):
        self.point_list.append((x, y))

    def is_not_empty(self):
        return len(self.point_list) != 0


class MyScene(QtWidgets.QGraphicsScene):
    last_point = None
    first_point = None
    link_dist = 10

    edge_color = Qt.red
    edge_pen = QPen(edge_color)
    edge_pen.setWidth(1)

    fill_color = Qt.white
    fill_pen = QPen(fill_color)
    fill_pen.setWidth(1)

    image = QImage()
    image_size = (0, 0)
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0

    def setup(self, bg_color, x_size, y_size):
        self.image_size = (x_size, y_size)
        self.max_x, self.max_y = x_size - 1, y_size - 1

        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))

        self.clear_image()
        # По заданию нужно было показать заполнение на кривой
        # Для отрисовки эллипса просто разкоментировать строку)
        # self.drawe_canonical(300, 300, 200, 140)
        self.update_image()

    def clear(self, clear_image=True):
        super().clear()
        if clear_image:
            self.last_point = None
            self.first_point = None
            self.clear_image()

    # Clear the QImage (delete all pixels)
    def clear_image(self):
        self.image = QImage(*self.image_size, QImage.Format_RGB32)

    # Set the brush's colors
    def set_edge_color(self, color):
        self.edge_color = color
        self.edge_pen.setColor(QColor(color))

    def set_fill_color(self, color):
        self.fill_color = color
        self.fill_pen.setColor(QColor(color))

    # Input edges function
    def input_point(self, point, is_orto, color):
        if self.first_point is None:
            self.first_point = point
            self.last_point = point
            self.set_edge_color(color)
            return

        if is_orto:
            dx = point[0] - self.last_point[0]
            dy = point[1] - self.last_point[1]
            # Горизонтальная линия
            if abs(dx) > abs(dy):
                point[1] = self.last_point[1]
            else:
                point[0] = self.last_point[0]

        if self.is_closed(point):  # and not is_orto:
            point = self.first_point
            self.add_edge(self.last_point, point)
            self.last_point = None
            self.first_point = None
            # self.fill_sorted_list()
        else:
            self.add_edge(self.last_point, point)
            self.last_point = point

    def is_closed(self, point):
        x_into = abs(self.first_point[0] - point[0]) < self.link_dist
        y_into = abs(self.first_point[1] - point[1]) < self.link_dist
        return x_into and y_into

    def add_edge(self, p1, p2):
        if p1 == p2:
            return
        self.draw_DDP(p1, p2)
        self.update_image()

    # !!!
    # Fill figure function
    # !!!
    def string_fill(self, x0, y0, delay=0):
        stack = Stack()
        stack.push(x0, y0)
        while stack.is_not_empty():
            x, y = stack.pop()
            if self.is_border_pixel(x, y) or self.is_fill_pixel(x, y):
                continue
            self.draw_fill_pixel(x, y)

            right_x = self.fill_line_right(x + 1, y)
            left_x = self.fill_line_left(x - 1, y)

            self.add_new_points(stack, left_x, right_x, y + 1)
            self.add_new_points(stack, left_x, right_x, y - 1)

            if delay != 0:  # Задержка
                self.make_delay(delay)
                self.update_image()

    def add_new_points(self, stack, left_x, right_x, y):
        if not self.min_y <= y <= self.max_y:
            return
        x = left_x
        while x <= right_x:
            flag = False
            # Переход к самому правому пикселю незаполненой области
            while x <= right_x and not self.is_border_pixel(x, y) \
                    and not self.is_fill_pixel(x, y):
                flag = True
                x += 1

            # Если пиксель найден, то заносится в стек
            if flag:
                if x == right_x and not self.is_border_pixel(x, y) \
                        and not self.is_fill_pixel(x, y):
                    print("Bruh")
                    stack.push(x, y)
                else:
                    stack.push(x - 1, y)

            # Переход к следующей незаполненной области
            temp_x = x
            while (self.is_border_pixel(x, y) or self.is_fill_pixel(x, y)) \
                    and x < right_x:
                x += 1
            if temp_x == x:
                x += 1

    def fill_line_right(self, x, y):
        while not self.is_border_pixel(x, y) and x < self.max_x:
            self.draw_fill_pixel(x, y)
            x += 1
        right_x = x - 1
        return right_x

    def fill_line_left(self, x, y):
        while not self.is_border_pixel(x, y) and x > self.min_x:
            self.draw_fill_pixel(x, y)
            x -= 1
        left_x = x + 1
        return left_x

    # Drawing pixels
    def draw_edge_pixel(self, x, y):
        self.image.setPixelColor(x, y, self.edge_color)
    def draw_fill_pixel(self, x, y):
        self.image.setPixelColor(x, y, self.fill_color)

    # Scanning pixels
    def is_border_pixel(self, x, y):
        return self.image.pixelColor(x, y) == self.edge_color
    def is_fill_pixel(self, x, y):
        return self.image.pixelColor(x, y) == self.fill_color

    # Figures drawing
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
