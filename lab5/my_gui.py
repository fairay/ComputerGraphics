from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from math import *
from time import *
from matplotlib import pyplot


class GuiMainWin(Ui_MainWindow):
    # TODO delete last_point
    scene = None
    last_point = None
    scene_bg_color = Qt.black
    drawEllipseArr = []
    drawCircleArr = []
    centerEntries = []

    def setupUi(self, MainWindow):
        # TODO delete all of the trash
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        self.scene.setup(self.scene_bg_color)
        self.graphicsView.setScene(self.scene)
        self.set_binds()

    def show_error(self, err_text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">{:} </span></p></body></html>".format(err_text))
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def draw_point(self, x, y, is_orto):
        x -= self.graphicsView.pos().x()
        x -= int(self.graphicsView.size().width() / 2)
        if abs(x) > int(self.graphicsView.size().width() / 2):
            return
        x -= 6

        y -= self.graphicsView.pos().y()
        y -= int(self.graphicsView.size().height() / 2)
        if abs(y) > int(self.graphicsView.size().height() / 2):
            return
        y -= 5

        self.scene.input_point([x, y], is_orto, self.get_edge_color())

    def set_binds(self):
        self.exploreTime.clicked.connect(self.cmp_time)
        self.clearCanvas.clicked.connect(self.clear_scene)
        self.fillImage.clicked.connect(self.fill_image)

    def get_mode(self):
        return self.modeSwitch.currentIndex()

    def get_fill_color(self):
        color = None
        if self.redSwitch.isChecked():      color = Qt.red
        elif self.greenSwitch.isChecked():  color = Qt.green
        elif self.blueSwitch.isChecked():   color = Qt.blue
        elif self.blackSwitch.isChecked():  color = Qt.white
        return color

    def get_edge_color(self):
        color = None
        if self.redSwitch_4.isChecked():
            color = Qt.red
        elif self.greenSwitch_4.isChecked():
            color = Qt.green
        elif self.blueSwitch_4.isChecked():
            color = Qt.blue
        elif self.blackSwitch_4.isChecked():
            color = Qt.white
        return color

    def get_center_point(self, n=0):
        x = int(self.centerEntries[n][0].text())
        y = int(self.centerEntries[n][1].text())
        return x, y
    def get_radius(self):
        return int(self.radius.text())
    def get_r_min_max(self):
        r_min = int(self.min_r.text())
        r_max = int(self.max_r.text())
        return r_min, r_max
    def get_step_r(self):
        return int(self.step_r.text())
    def get_ab(self):
        a = int(self.x_size.text())
        b = int(self.y_size.text())
        return a, b
    def get_ab_min(self):
        a = int(self.x_size_2.text())
        b = int(self.y_size_2.text())
        return a, b
    def get_a_step(self):
        return int(self.x_step.text())
    def get_cir_amount(self):
        return int(self.cir_amount.text())
    def get_el_amount(self):
        return int(self.el_amount.text())

    def draw_all(self, bg):
        if bg:  color = None
        else:   color = self.get_core_color()
        self.scene.set_color(color)

        mode = self.get_mode()
        if mode == 0:
            self.draw_circle()
        elif mode == 1:
            self.draw_concentric_circles()
        elif mode == 2:
            self.draw_ellipse()
        elif mode == 3:
            self.draw_concentric_ellipses()

    def clear_scene(self):
        self.scene.clear()

    def time_square(self, func):
        i = 0
        t = time()
        while time() - t < 0.01 and i < 25:
            func()
            i += 1
        return (time() - t) / i

    def time_square_arr(self, a_arr, scene):
        time_arr = [0] * len(a_arr)
        for i in range(len(a_arr)):
            scene.add_edge((0, 0), (a_arr[i], 0))
            scene.add_edge((0, 0), (0, a_arr[i]))
            scene.add_edge((a_arr[i], a_arr[i]), (a_arr[i], 0))
            scene.add_edge((a_arr[i], a_arr[i]), (0, a_arr[i]))

            time_arr[i] = self.time_square(scene.fill_sorted_list)

            scene.clear()
            print(a_arr[i])
        return time_arr

    def cmp_time(self):
        cmp_canvas = MyScene()
        cmp_canvas.setup(Qt.white)
        a_arr = [10 + i*15 for i in range(20)]

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

    def fill_image(self):
        delay = self.horizontalSlider.value()
        self.scene.set_fill_color(self.get_fill_color())
        self.scene.fill_sorted_list(delay)
