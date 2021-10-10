from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from math import *
from time import *
from matplotlib import pyplot


class GuiMainWin(Ui_MainWindow):
    scene_bg_color = Qt.black
    drawEllipseArr = []
    drawCircleArr = []
    centerEntries = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        self.scene.setup(self.scene_bg_color,
                         x=780/2, y=730/2)
        self.graphicsView.setScene(self.scene)
        self.set_binds()

        self.drawCircleArr = self.scene.get_draw_circle()
        self.drawEllipseArr = self.scene.get_draw_ellipse()
        self.centerEntries = [(self.x_center, self.y_center),
                              (self.x_center_2, self.y_center_2),
                              (self.x_center_3, self.y_center_3),
                              (self.x_center_4, self.y_center_4)]

    def show_error(self, err_text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">{:} </span></p></body></html>".format(err_text))
        msg.setWindowTitle("Ошибка")
        msg.exec_()


    def set_binds(self):
        self.drawColor.clicked.connect(lambda:  self.draw_all(bg=False))
        self.drawBg.clicked.connect(lambda:     self.draw_all(bg=True))

        self.exploreTime.clicked.connect(self.cmp_time)
        self.clearCanvas.clicked.connect(self.clear_scene)

    def get_mode(self):
        return self.modeSwitch.currentIndex()

    def get_core_color(self):
        color = None
        if self.redSwitch.isChecked():      color = Qt.red
        elif self.greenSwitch.isChecked():  color = Qt.green
        elif self.blueSwitch.isChecked():   color = Qt.blue
        elif self.blackSwitch.isChecked():  color = Qt.white
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

    """
    def drawCircle(self, isCore=1):
        if isCore:  color = self.get_core_color()
        else:       color = None
        self.scene.set_color(color)

        x, y = self.get_center_point()
        r = self.get_radius()

        index = self.coreBox.currentIndex()

        draw_func = self.drawFuncArr[index]
        draw_func(x, y, r)

    def drawBeams(self, isCore=1):
        if isCore:  color = self.get_core_color()
        else:       color = None
        self.scene.set_color(color)

        if isCore:  index = self.coreBox.currentIndex()
        else:       index = self.compareBox.currentIndex()
        draw_func = self.drawFuncArr[index]

        p_center = self.get_center_point()
        step = self.get_beam_step()
        length = self.get_beam_len()

        if step < 0.5 or step > 360:
            self.show_error("Некорректный шаг!")
            return
        elif length < 1:
            self.show_error("Некорректная длина!")
            return

        angele = 0
        p_end = Point(p_center.x, p_center.y)
        while (angele < 360):
            p_end.x = round(p_center.x + length * cos(radians(angele)))
            p_end.y = round(p_center.y + length * sin(radians(angele)))
            draw_func(p_center, p_end)
            angele += step
    """

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

    def draw_circle(self):
        x, y = self.get_center_point(0)
        r = self.get_radius()

        alg_n = self.algBox.currentIndex()
        draw_func = self.drawCircleArr[alg_n]

        draw_func(x, y, r)

    def draw_concentric_circles(self):
        x, y = self.get_center_point(1)
        r_min, r_max = self.get_r_min_max()
        n = self.get_cir_amount()

        alg_n = self.algBox.currentIndex()
        draw_func = self.drawCircleArr[alg_n]

        step = (r_max - r_min) / (n - 1)
        for i in range(n):
            r = round(r_min + step * i)
            draw_func(x, y, r)

    def draw_ellipse(self):
        x, y = self.get_center_point(2)
        a, b = self.get_ab()

        alg_n = self.algBox.currentIndex()
        draw_func = self.drawEllipseArr[alg_n]

        draw_func(x, y, a, b)

    def draw_concentric_ellipses(self):
        x, y = self.get_center_point(3)
        a, b = self.get_ab_min()
        a_step = self.get_a_step()
        b_step = b * (a_step / a)
        n = self.get_el_amount()

        alg_n = self.algBox.currentIndex()
        draw_func = self.drawEllipseArr[alg_n]

        for i in range(n):
            draw_func(x, y, a, round(b + b_step*i))
            a += a_step

    def clear_scene(self):
        self.scene.clear()

    #
    # Замеры времени круга
    def timec_r(self, func, r):
        i = 0
        t = time()
        while time() - t < 0.01:
            func(0, 0, r)
            i += 1
        return (time() - t) / i

    def timec_r_arr(self, func, r_arr, clear):
        time_arr = [0] * len(r_arr)
        print(func)
        for i in range(len(r_arr)):
            time_arr[i] = self.timec_r(func, r_arr[i])
            clear()
            print(r_arr[i])
        return time_arr

    # Замеры времени
    def timee_r(self, func, a, b):
        i = 0
        t = time()
        while time() - t < 0.01:
            func(0, 0, a, b)
            i += 1
        return (time() - t) / i

    def timee_r_arr(self, func, a_arr, b_arr, clear):
        time_arr = [0] * len(a_arr)
        print(func)
        for i in range(len(a_arr)):
            time_arr[i] = self.timee_r(func, a_arr[i], b_arr[i])
            clear()
            print(a_arr[i], b_arr[i])
        return time_arr

    def cmp_time(self):
        point_n = 10
        legend_arr = ["Каноническое", "Параметрическое", "Брезенхем",
                      "Средняя точка", "Qt метод"]
        cmp_canvas = MyScene()
        cmp_canvas.setup(Qt.white, draw=True)
        r_arr = [10 + i*20 for i in range(point_n)]

        t = list()
        for func in cmp_canvas.get_draw_circle():
            t.append(self.timec_r_arr(func, r_arr, cmp_canvas.clear))
        print("OK")
        pyplot.close()
        pyplot.title("Исследование времени работы алгоритмов", fontsize=20)
        pyplot.get_current_fig_manager().resize(1500, 800)

        pyplot.subplot(1, 2, 1)
        pyplot.plot(r_arr, t[0], 'r')
        pyplot.plot(r_arr, t[1], 'g')
        pyplot.plot(r_arr, t[2], 'b')
        pyplot.plot(r_arr, t[3], 'm')
        pyplot.plot(r_arr, t[4], 'y')

        pyplot.title("Исследование времени работы алгоритмов\n"
                     "Рисование окружности", fontsize=20)
        pyplot.ylabel("t (секунды)", fontsize=20)
        pyplot.xlabel("r (пиксели)", fontsize=20)
        pyplot.legend(legend_arr)

        b_arr = [10 + i * 15 for i in range(point_n)]

        print("OKEY")
        t = list()
        for func in cmp_canvas.get_draw_ellipse():
            t.append(self.timee_r_arr(func, r_arr, b_arr, cmp_canvas.clear))
        print("OK")
        pyplot.subplot(1, 2, 2)
        pyplot.plot(r_arr, t[0], 'r')
        pyplot.plot(r_arr, t[1], 'g')
        pyplot.plot(r_arr, t[2], 'b')
        pyplot.plot(r_arr, t[3], 'm')
        pyplot.plot(r_arr, t[4], 'y')

        pyplot.title("Исследование времени работы алгоритмов\n"
                     "Рисование эллипса (a/b = 4/3)", fontsize=20)
        pyplot.ylabel("t (секунды)", fontsize=20)
        pyplot.xlabel("r (пиксели)", fontsize=20)
        pyplot.legend(legend_arr)

        pyplot.show()
