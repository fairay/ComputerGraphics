from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QGuiApplication
from math import *
from time import *
from matplotlib import pyplot


def f5(x, z):
    return sin(x*z)
    val = 0
    if x > 0:
        if z > 0:
            val = 2
        else:
            val = -1.5
    else:
        if z > 0:
            val = -1
        else:
            val = 1
    return val


class GuiMainWin(Ui_MainWindow):
    scene = None
    scene_bg_color = Qt.black
    f_arr = [
        lambda x, z: x*x + z*z,
        lambda x, z: sin(sqrt(x*x + z*z)),
        lambda x, z: sqrt(abs(1 + z*z - x*x)),
        lambda x, z: x + z,
        lambda x, z: sin(x*z)
    ]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        size_x = self.graphicsView.size().width()
        size_y = self.graphicsView.size().height()

        self.graphicsView.setSceneRect(0, 0, size_x-4, size_y-4)

        self.scene.setup(self.scene_bg_color, (size_x, size_y))
        self.graphicsView.setScene(self.scene)

        self.set_binds()

    def set_binds(self):
        self.drawButton.clicked.connect(self.draw_begin)
        self.clearCanvas.clicked.connect(self.clear_scene)

        self.ox_rotate.valueChanged.connect(self.draw_begin)
        self.oy_rotate.valueChanged.connect(self.draw_begin)
        self.oz_rotate.valueChanged.connect(self.draw_begin)

    def clear_scene(self):
        self.ox_rotate.setValue(0)
        self.oy_rotate.setValue(0)
        self.oz_rotate.setValue(0)
        self.scene.clear()

    def get_current_func(self):
        return self.f_arr[self.func_switch.currentIndex()]
    def get_x_params(self):
        begin = float(self.x_begin.text())
        end = float(self.x_end.text())
        n = int(self.x_step.value())
        step = (end - begin) / n
        return (begin, end, step)
    def get_z_params(self):
        begin = float(self.z_begin.text())
        end = float(self.z_end.text())
        n = int(self.z_step.value())
        step = (end - begin) / n
        return (begin, end, step)
    def get_rotate(self):
        ox = radians(float(self.ox_rotate.value()))
        oy = radians(float(self.oy_rotate.value()))
        oz = radians(float(self.oz_rotate.value()))
        return (ox, oy, oz)

    def draw_begin(self):
        func = self.get_current_func()

        x_par = self.get_x_params()
        z_par = self.get_z_params()
        angles = self.get_rotate()
        print(angles)
        self.scene.clear()
        self.scene.draw_surface(func, angles, x_par, z_par)

    def err_msg(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">"
            "{:}"
            " </span></p></body></html>".format(text))
        msg.setWindowTitle("Ошибка")
        msg.exec_()
