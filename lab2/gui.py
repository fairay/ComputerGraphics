# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from vals import *
from geometry import *
from math import *
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    MOVE_MODE =     0
    SCALE_MODE =    1
    ROTATE_MODE =   2

    def setupUi(self, MainWindow):
        self.mode = self.MOVE_MODE

        self.drawUi(MainWindow)
        self.setEntryStart()
        self.set_binds()

        self.reset_image()
        self.save_image()

    # Widgets
    def drawUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1200, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 850))
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.trans_butt = QtWidgets.QPushButton(self.centralwidget)
        self.trans_butt.setMinimumSize(QtCore.QSize(151, 55))
        self.trans_butt.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.trans_butt.setFont(font)
        self.trans_butt.setObjectName("trans_butt")
        self.gridLayout.addWidget(self.trans_butt, 3, 2, 1, 2)


        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)
        self.scene.setSceneRect(-10, -10, 10, 10)


        self.canvas = QtWidgets.QGraphicsView(self.scene)
        self.canvas.setSceneRect(-10, -10, 10, 10)
        self.canvas.setMinimumSize(QtCore.QSize(canvas_x, canvas_y))
        self.canvas.setMaximumSize(QtCore.QSize(canvas_x, canvas_y))
        self.canvas.setMouseTracking(False)
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 1, 4, 3, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.undo_butt = QtWidgets.QPushButton(self.centralwidget)
        self.undo_butt.setMinimumSize(QtCore.QSize(91, 55))
        self.undo_butt.setMaximumSize(QtCore.QSize(91, 45))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.undo_butt.setFont(font)
        self.undo_butt.setObjectName("undo_butt")
        self.gridLayout.addWidget(self.undo_butt, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.setupMoveFrame()
        self.setupScaleFrame()
        self.setupRotateFrame()

        self.gridLayout.addWidget(self.move_frame, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.scale_frame, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.rotate_frame, 2, 0, 1, 4)

        self.move_frame.setVisible(1)
        self.scale_frame.setVisible(0)
        self.rotate_frame.setVisible(0)

        # self.gridLayout.removeWidget(self.move_frame)

        self.reset_butt = QtWidgets.QPushButton(self.centralwidget)
        self.reset_butt.setMinimumSize(QtCore.QSize(120, 55))
        self.reset_butt.setMaximumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.reset_butt.setFont(font)
        self.reset_butt.setObjectName("reset_butt")
        self.gridLayout.addWidget(self.reset_butt, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(583, 50))
        self.label.setMaximumSize(QtCore.QSize(583, 50))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 6, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        menu_font = QtGui.QFont()
        menu_font.setPointSize(13)
        self.menubar.setFont(menu_font)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setMinimumSize(QtCore.QSize(583, 30))
        self.menubar.setObjectName("menubar")

        self.menu_1 = QtWidgets.QAction("Условие задачи")
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QAction("Управление")
        self.menu_2.setObjectName("menu_2")

        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_1)
        self.menubar.addAction(self.menu_2)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.movex_entry)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setEntryStart(self):
        self.movex_entry.setText("0")
        self.movey_entry.setText("0")

        self.scalex_entry.setText("0")
        self.scaley_entry.setText("0")
        self.scalekx_entry.setText("1.0")
        self.scaleky_entry.setText("1.0")

        self.rotatex_entry.setText("0")
        self.rotatey_entry.setText("0")
        self.rotatea_entry.setText("0")

    def setupScaleFrame(self):
        val = QtGui.QDoubleValidator()
        val.setLocale(QtCore.QLocale(QtCore.QLocale.English))

        self.scale_frame = QtWidgets.QFrame(self.centralwidget)
        self.scale_frame.setEnabled(True)
        self.scale_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scale_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scale_frame.setObjectName("scale_frame")
        self.formLayout = QtWidgets.QFormLayout(self.scale_frame)
        self.formLayout.setObjectName("formLayout")
        self.label_14 = QtWidgets.QLabel(self.scale_frame)
        self.label_14.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.label_13 = QtWidgets.QLabel(self.scale_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.scalex_entry = QtWidgets.QLineEdit(self.scale_frame)
        self.scalex_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.scalex_entry.setObjectName("scalex_entry")
        self.scalex_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.scalex_entry)

        self.label_15 = QtWidgets.QLabel(self.scale_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.scaley_entry = QtWidgets.QLineEdit(self.scale_frame)
        self.scaley_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.scaley_entry.setObjectName("scaley_entry")
        self.scaley_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.scaley_entry)
        self.line_2 = QtWidgets.QFrame(self.scale_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_16 = QtWidgets.QLabel(self.scale_frame)
        self.label_16.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.scale_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.scalekx_entry = QtWidgets.QLineEdit(self.scale_frame)
        self.scalekx_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.scalekx_entry.setObjectName("scalekx_entry")
        self.scalekx_entry.setValidator(val)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.scalekx_entry)
        self.label_18 = QtWidgets.QLabel(self.scale_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.scaleky_entry = QtWidgets.QLineEdit(self.scale_frame)
        self.scaleky_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.scaleky_entry.setObjectName("scaleky_entry")
        self.scaleky_entry.setValidator(val)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.scaleky_entry)

    def setupMoveFrame(self):
        self.move_frame = QtWidgets.QFrame(self.centralwidget)
        self.move_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.move_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.move_frame.setObjectName("move_frame")
        self.formLayout = QtWidgets.QFormLayout(self.move_frame)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.move_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_3)
        self.movex_entry = QtWidgets.QLineEdit(self.move_frame)
        self.movex_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.movex_entry.setObjectName("movex_entry")
        self.movex_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.movex_entry)
        self.label_5 = QtWidgets.QLabel(self.move_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_5)
        self.movey_entry = QtWidgets.QLineEdit(self.move_frame)
        self.movey_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.movey_entry.setObjectName("movey_entry")
        self.movey_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.movey_entry)
        self.label_4 = QtWidgets.QLabel(self.move_frame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.label_4)

    def setupRotateFrame(self):
        self.rotate_frame = QtWidgets.QFrame(self.centralwidget)
        self.rotate_frame.setEnabled(True)
        self.rotate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rotate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rotate_frame.setObjectName("rotate_frame")
        self.formLayout = QtWidgets.QFormLayout(self.rotate_frame)
        self.formLayout.setObjectName("formLayout")
        self.label_24 = QtWidgets.QLabel(self.rotate_frame)
        self.label_24.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_24)
        self.label_23 = QtWidgets.QLabel(self.rotate_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.rotatex_entry = QtWidgets.QLineEdit(self.rotate_frame)
        self.rotatex_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.rotatex_entry.setObjectName("rotatex_entry")
        self.rotatex_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rotatex_entry)
        self.label_25 = QtWidgets.QLabel(self.rotate_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.rotatey_entry = QtWidgets.QLineEdit(self.rotate_frame)
        self.rotatey_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.rotatey_entry.setObjectName("rotatey_entry")
        self.rotatey_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rotatey_entry)
        self.line_3 = QtWidgets.QFrame(self.rotate_frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.label_26 = QtWidgets.QLabel(self.rotate_frame)
        self.label_26.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.rotate_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.rotatea_entry = QtWidgets.QLineEdit(self.rotate_frame)
        self.rotatea_entry.setMaximumSize(QtCore.QSize(400, 30))
        self.rotatea_entry.setObjectName("rotatea_entry")
        self.rotatea_entry.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rotatea_entry)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.trans_butt.setText(_translate("MainWindow", "Преобразовать"))
        self.undo_butt.setText(_translate("MainWindow", "←"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">Выберете действие: </span></p></body></html>"))
        # self.reset_butt.setText(_translate("MainWindow", "↺"))
        self.reset_butt.setText(_translate("MainWindow", "Сброс"))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox.setItemText(self.MOVE_MODE, _translate("MainWindow", "Перемещение"))
        self.comboBox.setItemText(self.SCALE_MODE, _translate("MainWindow", "Масштабирование"))
        self.comboBox.setItemText(self.ROTATE_MODE, _translate("MainWindow", "Вращение"))
        self.label.setText(_translate("MainWindow", window_title_text))

        #
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Введите смещение:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Δx = </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Δy = </span></p></body></html>"))

        # Scale box labels
        self.label_14.setText(
            _translate("MainWindow",
                       "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Введите центр масштабировния:</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">x = </span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">y = </span></p></body></html>"))
        self.label_16.setText(
            _translate("MainWindow",
                       "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">Введите коэффициенты масштабировния:</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">kx = </span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">ky = </span></p></body></html>"))

        #
        self.label_24.setText(
            _translate("MainWindow",
                       "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Введите центр вращения:</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">x = </span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">y = </span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">Введите угол вращения: </span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-style:italic;\">угол θ° = </span></p></body></html>"))

    # Commands
    def set_binds(self):
        self.trans_butt.clicked.connect(self.trans_image)
        self.undo_butt.clicked.connect(self.undo_image)
        self.reset_butt.clicked.connect(self.reset_image)
        self.comboBox.currentIndexChanged.connect(self.switch_mode)

        self.menu_1.triggered.connect(self.show_task)
        self.menu_2.triggered.connect(self.show_control)

    def trans_image(self):
        try:
            if self.mode == self.MOVE_MODE:
                dx = int(self.movex_entry.text())
                dy = int(self.movey_entry.text())

                self.save_image()
                self.move_image(dx, dy)

            elif self.mode == self.SCALE_MODE:
                x = int(self.scalex_entry.text())
                y = int(self.scaley_entry.text())
                kx = float(self.scalekx_entry.text())
                ky = float(self.scaleky_entry.text())
                kx += 0 / kx
                ky += 0 / ky

                self.save_image()
                self.scale_image(x, y, kx, ky)

            elif self.mode == self.ROTATE_MODE:
                x = int(self.rotatex_entry.text())
                y = int(self.rotatey_entry.text())
                a = -int(self.rotatea_entry.text())

                self.save_image()
                self.rotate_image(x, y, a)

            self.draw_image()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(
                "<html><head/><body><p><span style=\" font-size:14pt;\">Некорректный формат ввода! </span></p></body></html>")
            msg.setWindowTitle("Ошибка")
            msg.exec_()

    def undo_image(self):
        self.load_image()
        self.draw_image()

    def reset_image(self):
        # Прямоугольник
        self.rect_arr = []
        for p in rect_zero:
            self.rect_arr.append(p.copy())

        # Астроида
        self.bx = bx_zero
        self.by = by_zero
        self.start_angle = start_angle_zero
        self.center = center_zero.copy()

        self.redraw_aster()
        self.draw_image()

    def switch_mode(self):
        new_mode = self.comboBox.currentIndex()
        self.move_frame.setVisible(0)
        self.scale_frame.setVisible(0)
        self.rotate_frame.setVisible(0)

        if new_mode == self.MOVE_MODE:
            self.move_frame.setVisible(1)
        elif new_mode == self.SCALE_MODE:
            self.scale_frame.setVisible(1)
        elif new_mode == self.ROTATE_MODE:
            self.rotate_frame.setVisible(1)

        self.mode = new_mode

    def show_task(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">\
            22) Нарисовать исходную фигуру, затем её переметить, \
            промасштабировать и повернуть. Фигура предстваляет собой\
            прямоугольник с внутренней астроидой<br><br>"
            "x = b * cos(t)^3 <br>\
            y = b * sin(t)^3 <br>\
            t - [0, 2pi]\
             </span></p></body></html>")
        msg.setWindowTitle("Условие задачи")
        msg.exec_()

    def show_control(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(
            "<html><head/><body><p><span style=\" font-size:14pt;\">\
            ← - вернуться на одно действие назад <br>\
            Сборос - вернуться к исходному изображению \
            </span></p></body></html>")
        msg.setWindowTitle("Условие задачи")
        msg.exec_()

    # Transformation
    def redraw_aster(self):
        self.aster_arr = []
        step = 2 / 3 / zero_R
        angle = 0

        while (angle < 360):
            x = (cos(radians(angle)) ** 3)
            y = (sin(radians(angle)) ** 3)

            p = Point(x, y)

            p.rotate_by(Point(0, 0), self.start_angle)
            p.scale_by(Point(0, 0), self.bx, self.by)
            p.move_by(self.center)

            self.aster_arr.append(p)

            angle += step

    def draw_image(self):
        self.scene.clear()
        oxy_size = 2
        oxy_pen = QPen(Qt.red)
        figure_brush = QBrush(Qt.black)
        figure_pen = QPen(Qt.black)
        figure_pen.setCapStyle(Qt.RoundCap)

        oxy_pen.setWidth(oxy_size)
        oxy_pen.setCapStyle(Qt.RoundCap)

        for x in range(x_min, x_max + 1):
            x_adp, y_apd = Point(x, 0).adp_xy()
            self.scene.addEllipse(x_adp, y_apd, 1, 1, oxy_pen, QBrush(Qt.red))
        for y in range(y_min, y_max + 1):
            x_adp, y_apd = Point(0, y).adp_xy()
            self.scene.addEllipse(x_adp, y_apd, 1, 1, oxy_pen, QBrush(Qt.red))

        self.scene.addLine(-1000, 0, 1000, 0, QPen(Qt.gray))
        self.scene.addLine(0, -1000, 0, 1000, QPen(Qt.gray))
        self.draw_text("X", canvas_x / 2 - 40, 0)
        self.draw_text("{:}".format(x_max), canvas_x / 2 - 40, -30)
        self.draw_text("{:}".format(x_min), -canvas_x / 2 + 10, -30)

        self.draw_text("Y", 0, -canvas_y / 2 + 10)
        self.draw_text("{:}".format(y_max), -30, -canvas_y / 2 + 10)
        self.draw_text("{:}".format(y_min), -30, canvas_y / 2 - 40)

        # Центр окружности
        oxy_pen = QPen(Qt.darkBlue)
        oxy_pen.setWidth(4)
        self.scene.addEllipse(*self.center.adp_xy(), 1, 1, oxy_pen, QBrush(Qt.red))

        # Астроида
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        path.clear()
        for p in self.aster_arr:
            path.lineTo(*p.adp_xy())
            # self.scene.addEllipse(x, y, 1, 1, figure_pen, figure_brush)
        path.closeSubpath()
        self.scene.addPath(path, figure_pen)

        # Прямоугольник
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        path.clear()
        for P in self.rect_arr:
            x, y = P.adp_xy()
            path.lineTo(x, y)
        path.closeSubpath()
        self.scene.addPath(path, figure_pen)

    def draw_text(self, text, x, y):
        text = self.scene.addText(text)
        text.setPos(x, y)

    def move_image(self, dx, dy):
        offset = Point(dx, dy)

        for p in self.rect_arr:
            p.move_by(offset)
        for p in self.aster_arr:
            p.move_by(offset)
        self.center.move_by(offset)

    def scale_image(self, x, y, kx, ky):
        center = Point(x, y)

        for p in self.rect_arr:
            p.scale_by(center, kx, ky)
        for p in self.aster_arr:
            p.scale_by(center, kx, ky)

        self.center.scale_by(center, kx, ky)

    def rotate_image(self, x, y, alpha):
        center = Point(x, y)

        for p in self.rect_arr:
            p.rotate_by(center, alpha)
        for p in self.aster_arr:
            p.rotate_by(center, alpha)

        self.center.rotate_by(center, alpha)

    def save_image(self):
        # Прямоугольник
        self.pre_rect_arr = []
        for p in self.rect_arr:
            self.pre_rect_arr.append(p.copy())

        # Астроида
        self.pre_aster_arr = []
        for p in self.aster_arr:
            self.pre_aster_arr.append(p.copy())
        self.pre_center = self.center.copy()
        

    def load_image(self):
        # Прямоугольник
        self.rect_arr = []
        for p in self.pre_rect_arr:
            self.rect_arr.append(p.copy())

        # Астроида
        self.aster_arr = []
        for p in self.pre_aster_arr:
            self.aster_arr.append(p.copy())
        self.center = self.pre_center.copy()

