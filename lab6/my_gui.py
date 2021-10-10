from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QGuiApplication
from math import *
from time import *
from matplotlib import pyplot


class GuiMainWin(Ui_MainWindow):
    scene = None
    fill_mode = False
    scene_bg_color = Qt.black
    drawEllipseArr = []
    drawCircleArr = []
    centerEntries = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        size_x = self.graphicsView.size().width()
        size_y = self.graphicsView.size().height()

        self.graphicsView.setSceneRect(0, 0, size_x-4, size_y-4)

        self.scene.setup(self.scene_bg_color, size_x, size_y)
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

        if self.fill_mode:
            # Заполнение фигуры
            self.fill_begin((x, y))
        else:
            # Добавление ребра
            self.scene.input_point([x, y], is_orto, self.get_edge_color())

    def set_binds(self):
        self.exploreTime.clicked.connect(self.cmp_time)
        self.clearCanvas.clicked.connect(self.clear_scene)
        self.fillImage.clicked.connect(self.fill_mode_on)

    # Считывание цветов с виджетов
    def get_fill_color(self):
        color = None
        if self.redSwitch.isChecked():      color = Qt.red
        elif self.greenSwitch.isChecked():  color = Qt.green
        elif self.blueSwitch.isChecked():   color = Qt.blue
        elif self.blackSwitch.isChecked():  color = Qt.white
        return color

    def get_edge_color(self):
        color = None
        if self.redSwitch_4.isChecked():        color = Qt.red
        elif self.greenSwitch_4.isChecked():    color = Qt.green
        elif self.blueSwitch_4.isChecked():     color = Qt.blue
        elif self.blackSwitch_4.isChecked():    color = Qt.white
        return color

    def clear_scene(self):
        self.scene.clear()

    # Функции замера времени
    def time_square(self, func, x0, y0):
        i = 0
        t = time()
        while time() - t < 0.01 and i < 50:
            func(x0, y0)
            i += 1
        return (time() - t) / i

    def time_square_arr(self, a_arr, scene):
        time_arr = [0] * len(a_arr)
        for i in range(len(a_arr)):
            a = a_arr[i]
            scene.add_edge((0, 0), (a, 0))
            scene.add_edge((0, 0), (0, a))
            scene.add_edge((a, a), (a, 0))
            scene.add_edge((a, a), (0, a))

            x_0 = int(a/2)
            time_arr[i] = self.time_square(scene.string_fill, x_0, x_0)

            scene.clear()
            print(a_arr[i], "=", time_arr[i])
        return time_arr

    def cmp_time(self):
        cmp_canvas = MyScene()
        cmp_canvas.setup(Qt.black, 500, 500)
        a_arr = [10 + i*20 for i in range(20)]

        t_arr = self.time_square_arr(a_arr, cmp_canvas)
        pyplot.close()
        pyplot.get_current_fig_manager().resize(1000, 900)

        area_arr = [i*i for i in a_arr]
        pyplot.plot(area_arr, t_arr, 'r')
        pyplot.title("Исследование времени работы алгоритма\n"
                     "в зависимости от площади\n"
                     "на примере квадратной области", fontsize=20)
        pyplot.ylabel("t (секунды)", fontsize=20)
        pyplot.xlabel("S (пиксели)", fontsize=20)

        pyplot.show()

    # Включение режима введения затравочной точки
    def fill_mode_on(self):
        self.fill_mode = True
        QGuiApplication.setOverrideCursor(QCursor(Qt.CrossCursor))

    # Заливка фигуры
    def fill_begin(self, point):
        self.fill_mode = False
        QGuiApplication.restoreOverrideCursor()

        delay = self.horizontalSlider.value()
        self.scene.set_fill_color(self.get_fill_color())
        self.scene.string_fill(*point, delay)

        self.scene.update_image()
