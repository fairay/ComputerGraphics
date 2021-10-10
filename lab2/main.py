# Лабораторная работа №2

# 22)
# Нарисовать исходную фигуру, затем её переметить, \
# промасштабировать и повернуть. Фигура предстваляет собой прямоугольник с \
# внутренней астроидой
# x = b * cos(t)^3
# y = b * sin(t)^3,
# t - [0, 2pi]

from math import *
import sys
from PyQt5 import QtWidgets, QtGui

from geometry import *
from vals import *
from gui import *

app, application = None, None


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



def main():
    global app, application
    app = QtWidgets.QApplication([])
    application = MainWin()
    application.show()

    v = QtGui.QDoubleValidator()
    sys.exit(app.exec())

main()
