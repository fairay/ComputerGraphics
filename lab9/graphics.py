from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QBrush, QPen, QColor, QImage
from math import *


class MyScene(QtWidgets.QGraphicsScene):
    segment_arr = []
    first_point = None
    link_dist = 10

    cut_arr = []
    cut_obj = []
    cut_p1 = None
    cut_plast = None

    polygon_arr = []
    polygon_obj = []
    polygon_p1 = None
    polygon_plast = None

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
            self.clear_polygon()
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
    def is_closed(self, first_point, point):
        x_into = abs(first_point[0] - point[0]) < self.link_dist
        y_into = abs(first_point[1] - point[1]) < self.link_dist
        return x_into and y_into

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

    def add_poly_edge(self, p1, p2):
        if p1 == p2: return

        draw_obj = self.addLine(*p1, *p2, self.edge_pen)

        self.polygon_obj.append(draw_obj)
        self.polygon_arr.append((p1, p2))

    def add_poly_point(self, point, is_orto, color):
        if self.polygon_p1 is None:
            self.set_edge_color(color)
            if len(self.polygon_arr) != 0:
                self.clear_polygon()
            self.polygon_p1 = point
            self.polygon_plast = point
            return

        if is_orto:
            dx = point[0] - self.polygon_plast[0]
            dy = point[1] - self.polygon_plast[1]
            # Горизонтальная линия
            if abs(dx) > abs(dy):
                point[1] = self.polygon_plast[1]
            else:
                point[0] = self.polygon_plast[0]
        elif len(self.cut_arr):
            for cut_seg in self.cut_arr:
                if self.is_closed(cut_seg[0], point):
                    print("Hook the vertex")
                    point = cut_seg[0]
                    break
            else:
                for cut_seg in self.cut_arr:
                    edge_cross = cross_point(cut_seg, [self.polygon_plast, point])
                    if edge_cross is None: continue
                    if self.is_closed(edge_cross, point):
                        print("Hook the cross!")
                        point = edge_cross
                        break

        if self.is_closed(self.polygon_p1, point):
            point = self.polygon_p1

        self.add_poly_edge(self.polygon_plast, point)
        self.polygon_plast = point
        if point == self.polygon_p1:
            print(self.polygon_arr)
            self.polygon_p1 = None
            self.polygon_plast = None
        return

    def clear_cut(self):
        self.cut_p1 = None
        self.cut_plast = None
        for draw in self.cut_obj:
            self.removeItem(draw)
        self.cut_obj = []
        self.cut_arr = []

    def clear_polygon(self):
        self.polygon_p1 = None
        self.polygon_plast = None
        for draw in self.polygon_obj:
            self.removeItem(draw)
        self.polygon_obj = []
        self.polygon_arr = []

    #
    #   Cyrus - Beck cut algorithm
    #
    def sutherland_hodgman_cut(self):
        cut_dir = is_convex(self.cut_arr)
        if not cut_dir: return False
        
        np = len(self.polygon_arr)
        p = list(point[0] for point in self.polygon_arr)

        nc = len(self.cut_arr)
        c = list(point[0] for point in self.cut_arr)
        c.append(c[0])

        f, s = None, None
        for i in range(nc):
            nq = 0
            q = []
            for j in range(np):
                if j == 0:
                    f = p[0]
                elif is_cross((s, p[j]), (c[i], c[i+1])):
                    cross_p = find_cross((s, p[j]), (c[i], c[i+1]))
                    q.append(cross_p)
                    nq += 1

                s = p[j]
                if is_visible(s, (c[i], c[i+1])) * cut_dir >= 0:
                    q.append(s)
                    nq += 1

            if nq != 0 and is_cross((s, f), (c[i], c[i+1])):
                cross_p = find_cross((s, f), (c[i], c[i + 1]))
                q.append(cross_p)
                nq += 1
            p = q
            np = nq
            if np < 2: break

        for i in range(np):
            self.draw_line(p[i-1], p[i])
        return True

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


def is_visible(point, cut):
    temp1 = (point[0] - cut[0][0]) * (cut[1][1] - cut[0][1])
    temp2 = (point[1] - cut[0][1]) * (cut[1][0] - cut[0][0])
    return temp1 - temp2


def is_cross(seg, cut):
    view0 = is_visible(seg[0], cut)
    view1 = is_visible(seg[1], cut)
    return view0*view1 <= 0


def matrix_det(a, b, c, d):
    return a*d - b*c
def cross_point(edge, line):
    A1, B1, C1 = line_equation(*edge)
    A2, B2, C2 = line_equation(*line)

    det = matrix_det(A2, B2, A1, B1)
    if det == 0:
        point = line[1]
    else:
        point = [0, 0]
        point[0] = -matrix_det(C2, B2, C1, B1) / det
        point[1] = -matrix_det(A2, C2, A1, C1) / det

    if (point[0] - edge[0][0]) * (point[0] - edge[1][0]) <= 0 and \
            (point[1] - edge[0][1]) * (point[1] - edge[1][1]) <= 0:
        return point
    else:
        return None


def find_cross(edge1, edge2):
    A1, B1, C1 = line_equation(*edge1)
    A2, B2, C2 = line_equation(*edge2)

    det = matrix_det(A2, B2, A1, B1)
    if det == 0:
        return edge1[1]

    point = [0, 0]
    point[0] = -matrix_det(C2, B2, C1, B1) / det
    point[1] = -matrix_det(A2, C2, A1, C1) / det

    return point
