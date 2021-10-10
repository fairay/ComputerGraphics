from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor, QImage
from math import *

# EPS = 10e-3
EPS = 1


class MyScene(QtWidgets.QGraphicsScene):
    segment_arr = []
    first_point = None
    link_dist = 10

    cut_arr = []
    cut_obj = []
    cut_p1 = None
    cut_plast = None

    edge_color = Qt.red
    edge_pen = QPen(edge_color)
    edge_pen.setWidth(1)

    cut_color = Qt.white
    cut_pen = QPen(cut_color)

    result_color = Qt.yellow
    result_pen = QPen(result_color)

    inv_brush = QBrush(QColor(Qt.black))

    def setup(self, bg_color):
        self.bg_color = bg_color
        self.setBackgroundBrush(QBrush(bg_color))

        inv_color = QColor(bg_color)
        inv_color.setAlphaF(0)
        self.inv_brush = QBrush(inv_color)

    def clear(self, clear_image=True):
        if clear_image:
            self.segment_arr = []
            self.clear_cut()
            self.first_point = None
        super().clear()

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

    def is_closed(self, first_point, point):
        x_into = abs(first_point[0] - point[0]) < self.link_dist
        y_into = abs(first_point[1] - point[1]) < self.link_dist
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

    def add_cut_edge(self, p1, p2):
        if p1 == p2:
            return

        draw_obj = self.addLine(*p1, *p2, self.cut_pen)

        self.cut_obj.append(draw_obj)
        self.cut_arr.append((p1, p2))

    def add_cut_point(self, point, is_orto):
        if self.cut_p1 is None:
            self.cut_p1 = point
            self.cut_plast = point
            return

        if is_orto:
            dx = point[0] - self.cut_plast[0]
            dy = point[1] - self.cut_plast[1]
            # Горизонтальная линия
            if abs(dx) > abs(dy):
                point[1] = self.cut_plast[1]
            else:
                point[0] = self.cut_plast[0]

        if self.is_closed(self.cut_p1, point):
            point = self.cut_p1

        self.add_cut_edge(self.cut_plast, point)
        self.cut_plast = point
        if point == self.cut_p1:
            print(self.cut_arr)
        return point == self.cut_p1

    def clear_cut(self):
        self.cut_p1 = None
        self.cut_plast = None
        for draw in self.cut_obj:
            self.removeItem(draw)
        self.cut_obj = []
        self.cut_arr = []

    #
    #   Cyrus - Beck cut algorithm
    #
    def cut_segments(self):
        dir = is_convex(self.cut_arr)
        if not dir: return False
        n_arr = find_normals(self.cut_arr, dir == -1)

        for segment in self.segment_arr:
            self.cyrus_beck_cut(segment, n_arr)
        return True

    def cyrus_beck_cut(self, segment, n_arr):
        t0, t1 = 0, 1
        d = edge_dir(*segment)
        for i in range(len(self.cut_arr)):
            w = edge_dir(self.cut_arr[i][0], segment[0])

            d_mlt = scalar_mlt(d, n_arr[i])
            w_mlt = scalar_mlt(w, n_arr[i])
            if d_mlt == 0:
                if w_mlt < 0:   return
                else:           continue

            t = -w_mlt / d_mlt
            if d_mlt > 0:
                print(">0,", t)
                if t > 1: return
                t0 = max(t, t0)
            else:
                print("<0,", t)
                if t < 0: return
                t1 = min(t, t1)
        if t0 <= t1:
            p0 = edge_ratio(segment[0], d, t0)
            p1 = edge_ratio(segment[0], d, t1)
            self.draw_line(p0, p1)

    # Figures drawing
    def draw_line(self, p1, p2):
        self.addLine(*p1, *p2, self.result_pen)


def line_equation(p1, p2):
    A = p2[1] - p1[1]
    B = p1[0] - p2[0]
    C = -p1[0] * A - p1[1] * B
    return A, B, C

def edge_mid(p1, p2):
    p = [0, 0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
def edge_dir(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return [x, y]
def edge_normal(p1, p2):
    x = p2[1] - p1[1]
    y = p1[0] - p2[0]
    return [x, y]
def edge_ratio(p0, d, t):
    p = [0, 0]
    p[0] = p0[0] + d[0]*t
    p[1] = p0[1] + d[1]*t
    return p

def scalar_mlt(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]
def vector_mlt(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]
def neg_vector(v):
    return [-v[0], -v[1]]


def find_normals(edge_arr, is_invert):
    normal_arr = [None] * len(edge_arr)
    for i in range(len(edge_arr)):
        normal_arr[i] = edge_normal(*edge_arr[i])
        if is_invert:
            normal_arr[i] = neg_vector(normal_arr[i])
    return normal_arr

"""
p0 = edge_mid(*edge_arr[i-1])    # середина иного ребра
        p2 = edge_mid(*edge_arr[i])     # середина текущего ребра
        direct = edge_dir(p2, p0)

        print(normal_arr[i], direct)
        # if scalar_mlt(normal_arr[i], direct) < 0:
"""


def is_convex(edge_arr):
    v1 = edge_dir(*edge_arr[-1])
    v2 = edge_dir(*edge_arr[0])
    last_mlt = vector_mlt(v2, v1)

    for i in range(1, len(edge_arr)):
        v1 = edge_dir(*edge_arr[i - 1])
        v2 = edge_dir(*edge_arr[i])

        mlt = vector_mlt(v2, v1)
        if mlt * last_mlt <= 0:
            return False
        last_mlt = mlt
    return copysign(1, last_mlt)
