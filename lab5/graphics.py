from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor
from math import *
from edge_func import *

EPS = 10e-3


def round_down(x):
    return floor(x)
def round_up(x):
    return round(x+0.5)

class MyScene(QtWidgets.QGraphicsScene):
    edge_arr = []
    last_point = None
    first_point = None
    link_dist = 10

    edge_pen = QPen(Qt.white)
    edge_pen.setWidth(1)
    fill_pen = QPen(Qt.white)
    fill_pen.setWidth(1)
    brush = QBrush(Qt.black)
    color = QColor(Qt.black)

    def setup(self, bg_color, x=0, y=0):
        self.x_off = x
        self.y_off = y
        self.setSceneRect(-10, -10, 10, 10)
        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))
        self.init_brush()
        self.clear()

    def clear(self, clear_edges=True):
        super().clear()
        if clear_edges:
            self.edge_arr = []
        self.last_point = None
        self.first_point = None

    def init_brush(self):
        color = QColor(Qt.black)
        color.setAlphaF(0)
        self.brush.setColor(color)
        pass

    def set_edge_color(self, color):
        self.color = QColor(color)
        self.edge_pen.setColor(color)

    def set_fill_color(self, color):
        color = QColor(color)
        self.fill_pen.setColor(color)

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
        new_edge = Edge((p1[0], -p1[1]), (p2[0], -p2[1]))
        self.edge_arr.append(new_edge)
        # self.addLine(*p1, *p2, self.edge_pen)
        self.draw_DDP(p1, p2)

    def redraw_all_edges(self):
        # self.clear(clear_edges=False)
        for edge in self.edge_arr:
            self.draw_DDP((edge.x1, -edge.y1), (edge.x2, -edge.y2))
            # self.addLine(edge.x1, edge.y1, edge.x2, edge.y2, self.edge_pen)

    # Fill figure function
    def fill_sorted_list(self, delay=0):
        if not len(self.edge_arr):
            return  # В случае, если нет рёбер
        # Список активных рёбер
        lae = None

        # Формирование y-группы
        y_group = create_y_group(self.edge_arr)
        y = max(y_group.keys())
        y_min = find_min_y(self.edge_arr)

        while y > y_min:
            # Добавление новых элементов из y-группы
            if y in y_group.keys():
                for edge in y_group[y]:
                    lae = lae_add(lae, edge)
            # lae = sort_lae(lae)

            # Проход во всем точкам пересечения
            temp_edge = lae
            while temp_edge is not None and temp_edge.next is not None:
                next_edge = temp_edge.next
                if not is_match(temp_edge, next_edge):
                    # В случае, если точки не совпадают
                    if abs(temp_edge.dx) > 1:
                        x1 = round_down(temp_edge.x + abs(temp_edge.dx/2))
                    else:
                        x1 = round(temp_edge.x)

                    if abs(next_edge.dx) > 1:
                        x2 = round_up(next_edge.x - abs(next_edge.dx/2))
                    else:
                        x2 = round(next_edge.x)

                    self.draw_line(x1+1, x2-1, y)

                    temp_edge = next_edge.next
                    if temp_edge is not None and is_match(temp_edge, next_edge):
                        if not is_extremum(temp_edge.dy, next_edge.dy):
                            temp_edge = temp_edge.next
                        elif is_horisontal(temp_edge) or is_horisontal(next_edge):
                            temp_edge = temp_edge.next
                            if temp_edge is not None and temp_edge.dy == 0:
                                temp_edge = temp_edge.next
                else:
                    # В случае, если точки совпали
                    if is_horisontal(temp_edge) or is_horisontal(next_edge):
                        temp_edge = next_edge.next
                        if temp_edge is not None and temp_edge.dy == 0:
                            temp_edge = temp_edge.next
                    elif is_extremum(temp_edge.dy, next_edge.dy):
                        temp_edge = next_edge.next
                    else:
                        temp_edge = next_edge
            # Переход к следующей строке
            y -= 1
            lae = lae_step(lae)

            if delay != 0:  # Задержка
                self.make_delay(delay)

    def draw_pixel(self, x, y):
        self.addLine(x, y, x, y, self.fill_pen)
    def draw_edge_pixel(self, x, y):
        self.addLine(x, y, x, y, self.edge_pen)

    def draw_err_pixel(self, x, y):
        pen = QPen(Qt.yellow)
        self.addLine(x, y, x, y, pen)

    def draw_line(self, x1, x2, y):
        if x1 > x2:
            return
        # self.addLine(x1, -y, x2, -y, self.fill_pen)

        for x in range(x1, x2 + 1):
            self.draw_pixel(x, -y)

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

    def make_delay(self, delay):
        QtWidgets.QApplication.processEvents()
        QThread.msleep(delay)
