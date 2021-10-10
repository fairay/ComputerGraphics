from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QGuiApplication
from math import *
from time import *
from matplotlib import pyplot


class GuiMainWin(Ui_MainWindow):
    scene = None
    cut_rect_mode = False
    cut_rect_count = 0
    scene_bg_color = Qt.black

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        size_x = self.graphicsView.size().width()
        size_y = self.graphicsView.size().height()

        self.graphicsView.setSceneRect(0, 0, size_x-4, size_y-4)

        self.scene.setup(self.scene_bg_color)
        self.graphicsView.setScene(self.scene)

        self.set_binds()

    # При клике мыши
    def draw_point(self, x, y, is_orto):
        x -= self.graphicsView.pos().x()
        if not 0 <= x <= self.graphicsView.size().width():
            return
        x -= 0

        y -= self.graphicsView.pos().y()
        if not 0 <= y <= self.graphicsView.size().height():
            return
        y -= 2

        if self.cut_rect_mode:
            self.add_rect_point([x, y], is_orto)
        else:
            # Добавление ребра
            self.scene.input_point([x, y], is_orto, self.get_edge_color())

    def set_binds(self):
        # self.cutButton.clicked.connect(self.scene.mid_point_cut)
        self.cutButton.clicked.connect(self.cut_begin)
        self.clearCanvas.clicked.connect(self.clear_scene)
        self.inputCutButton.clicked.connect(self.cut_rect_on)

    # Считывание цветов с виджетов
    def get_cut_color(self):
        color = None
        if self.redSwitch.isChecked():      color = Qt.red
        elif self.greenSwitch.isChecked():  color = Qt.green
        elif self.blueSwitch.isChecked():   color = Qt.blue
        elif self.whiteSwitch.isChecked():  color = Qt.white
        return color

    def get_edge_color(self):
        color = None
        if self.redSwitch_2.isChecked():        color = Qt.red
        elif self.greenSwitch_2.isChecked():    color = Qt.green
        elif self.blueSwitch_2.isChecked():     color = Qt.blue
        elif self.whiteSwitch_2.isChecked():    color = Qt.white
        return color

    def clear_scene(self):
        self.scene.clear()

    # Включение режима введения затравочной точки
    def fill_mode_on(self):
        self.cut_rect_mode = True
        QGuiApplication.setOverrideCursor(QCursor(Qt.CrossCursor))

    # Отсечение отрезков
    def cut_begin(self):
        flag = self.scene.cut_segments()
        if not flag:
            self.err_msg("Невыпуклый отсекатель!")

    def cut_rect_on(self):
        self.cut_rect_mode = True
        self.cut_rect_count = 0
        QGuiApplication.setOverrideCursor(QCursor(Qt.CrossCursor))
        self.scene.set_cut_color(self.get_cut_color())
        self.scene.clear_cut()
    def cut_rect_off(self):
        self.cut_rect_mode = False
        self.cut_rect_count = 0
        QGuiApplication.restoreOverrideCursor()

    def add_rect_point(self, point, is_orto):
        flag = self.scene.add_cut_point(point, is_orto)
        if flag:
            self.cut_rect_off()

    def err_msg(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">"
            "{:}"
            " </span></p></body></html>".format(text))
        msg.setWindowTitle("Ошибка")
        msg.exec_()
