from ui.gui import *
from graphics import *

from PyQt5.QtCore import Qt
from math import *
from time import *
from matplotlib import pyplot


class GuiMainWin(Ui_MainWindow):
    # scene_bg_color = Qt.white
    scene_bg_color = Qt.black
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.scene = MyScene(self.centralwidget)
        self.scene.setup(self.scene_bg_color,
                         x=780/2, y=608/2)
        self.graphicsView.setScene(self.scene)

        self.set_binds()
        self.drawFuncArr = [self.scene.draw_DDP,
                            self.scene.draw_Bres_float,
                            self.scene.draw_Bres_int,
                            self.scene.draw_Bres_smooth,
                            self.scene.draw_Wu,
                            self.scene.draw_default]

    def set_binds(self):
        self.drawCoreLine.clicked.connect(lambda:   self.drawLine(isCore=1))
        self.drawCmpLine.clicked.connect(lambda:    self.drawLine(isCore=0))
        self.drawCoreRound.clicked.connect(lambda:  self.drawBeams(isCore=1))
        self.drawCmpRound.clicked.connect(lambda:   self.drawBeams(isCore=0))
        self.exploreTime.clicked.connect(self.cmp_time)
        self.exploreStep.clicked.connect(self.cmp_steps)
        self.clearCanvas.clicked.connect(self.clear_scene)

    def get_core_color(self):
        color = None
        if self.redSwitch.isChecked():      color = Qt.red
        elif self.greenSwitch.isChecked():  color = Qt.green
        elif self.blueSwitch.isChecked():   color = Qt.blue
        elif self.blackSwitch.isChecked():  color = Qt.white
        return color

    def get_st_point(self):
        x = int(self.x_start.text())
        y = int(self.y_start.text())
        return Point(x, y)
    def get_end_point(self):
        x = int(self.x_end.text())
        y = int(self.y_end.text())
        return Point(x, y)
    def get_center_point(self):
        x = int(self.x_center.text())
        y = int(self.y_center.text())
        return Point(x, y)
    def get_beam_step(self):
        return float(self.step_angle.text())
    def get_beam_len(self):
        return int(self.length.text())

    def drawLine(self, isCore=1):
        if isCore:  color = self.get_core_color()
        else:       color = None
        self.scene.set_color(color)

        p_st = self.get_st_point()
        p_end = self.get_end_point()

        if isCore:  index = self.coreBox.currentIndex()
        else:       index = self.compareBox.currentIndex()

        draw_func = self.drawFuncArr[index]
        draw_func(p_st, p_end)

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

    def clear_scene(self):
        self.scene.clear()

    def show_error(self, err_text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">{:} </span></p></body></html>".format(err_text))
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def count_time(self, func, length, step):
        p_start = Point(0, 0)
        p_end = Point(0, 0)
        angele = 0

        t = time()
        while angele < 2*pi:
            p_end.x = int(p_start.x + length * cos(angele))
            p_end.y = int(p_start.y + length * sin(angele))
            func(p_start, p_end)
            angele += step
        return time() - t

    def count_steps(self, func, angele_arr):
        p_start = Point(0, 0)
        p_end = Point(0, 0)
        length = 1000
        steps = []

        for angele in angele_arr:
            p_end.x = int(p_start.x + length * cos(radians(angele)))
            p_end.y = int(p_start.y + length * sin(radians(angele)))
            steps.append(func(p_start, p_end))
        return steps


    def cmp_time(self):
        print_arr = ["ЦДА", "Брезенхем\n(дробные)", "Брезенхем\n(целые)",
                     "Брезенхем\n(сглаживание)", "Ву", "Qt метод"]
        cmp_canvas = MyScene()
        cmp_canvas.setup(Qt.white, draw=True)
        length = 5000
        step = 1

        t = list()
        t.append(self.count_time(cmp_canvas.draw_DDP, length, step))
        t.append(self.count_time(cmp_canvas.draw_Bres_float, length, step))
        t.append(self.count_time(cmp_canvas.draw_Bres_int, length, step))
        t.append(self.count_time(cmp_canvas.draw_Bres_smooth, length, step))
        t.append(self.count_time(cmp_canvas.draw_Wu, length, step))
        t.append(self.count_time(cmp_canvas.draw_default, length, step))

        pyplot.close()
        pyplot.bar(print_arr, t)
        pyplot.get_current_fig_manager().resize(1200, 800)
        pyplot.title("Исследование времени работы алгоритмов\n\
        рисование пучка, длина {:} пикселей, шаг {:} рад.".format(length, step),
                     fontsize=20)
        pyplot.ylabel("t (секунды)", fontsize=20)
        pyplot.show()

    def cmp_steps(self):
        analysis = StepAnalysis()
        angle_arr = [i * 0.1 for i in range(901)]
        DDA_step = self.count_steps(analysis.DDA, angle_arr)
        Bres_int_step = self.count_steps(analysis.Bres_int, angle_arr)

        analysis = MaxLenAnalysis()
        DDA_len = self.count_steps(analysis.DDA, angle_arr)
        Bres_int_len = self.count_steps(analysis.Bres_int, angle_arr)

        pyplot.close()
        pyplot.get_current_fig_manager().resize(1200, 800)

        pyplot.subplot(1, 2, 1)
        pyplot.plot(angle_arr, DDA_step, 'r--')
        pyplot.plot(angle_arr, Bres_int_step, 'b--')
        pyplot.title("Количество ступенек \nна отрезке в 1000 пикселей", fontsize=20)
        pyplot.legend(["ЦДА", "Брезенхем"])

        pyplot.subplot(1, 2, 2)
        pyplot.plot(angle_arr, DDA_len, 'r--')
        pyplot.plot(angle_arr, Bres_int_len, 'b--')
        pyplot.title("Максимальная длина ступеньки \nна отрезке в 1000 пикселей", fontsize=20)
        pyplot.legend(["ЦДА", "Брезенхем"])
        pyplot.show()
