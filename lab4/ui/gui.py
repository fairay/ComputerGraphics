# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 800))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 255, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 215, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 117, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 215, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 255, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 215, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 117, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 215, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(197, 255, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 215, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 117, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 87, 68))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 175, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(459, 18, 770, 741))
        self.graphicsView.setMinimumSize(QtCore.QSize(700, 550))
        self.graphicsView.setMaximumSize(QtCore.QSize(10000, 10000))
        self.graphicsView.setObjectName("graphicsView")
        self.exploreTime = QtWidgets.QPushButton(self.centralwidget)
        self.exploreTime.setGeometry(QtCore.QRect(20, 650, 401, 51))
        self.exploreTime.setObjectName("exploreTime")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 530, 411, 101))
        self.groupBox.setObjectName("groupBox")
        self.drawColor = QtWidgets.QPushButton(self.groupBox)
        self.drawColor.setGeometry(QtCore.QRect(10, 40, 191, 51))
        self.drawColor.setObjectName("drawColor")
        self.drawBg = QtWidgets.QPushButton(self.groupBox)
        self.drawBg.setGeometry(QtCore.QRect(210, 40, 191, 51))
        self.drawBg.setObjectName("drawBg")
        self.clearCanvas = QtWidgets.QPushButton(self.centralwidget)
        self.clearCanvas.setGeometry(QtCore.QRect(20, 710, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.clearCanvas.setFont(font)
        self.clearCanvas.setAcceptDrops(False)
        self.clearCanvas.setObjectName("clearCanvas")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(430, -1, 21, 801))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 243, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 202, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 108, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 208, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 243, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 202, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 108, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(175, 208, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 243, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 202, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 108, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 81, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 162, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.line_4.setPalette(palette)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.algBox = QtWidgets.QComboBox(self.centralwidget)
        self.algBox.setGeometry(QtCore.QRect(20, 10, 411, 41))
        self.algBox.setObjectName("algBox")
        self.algBox.addItem("")
        self.algBox.addItem("")
        self.algBox.addItem("")
        self.algBox.addItem("")
        self.algBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 430, 411, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.blackSwitch = QtWidgets.QRadioButton(self.groupBox_2)
        self.blackSwitch.setGeometry(QtCore.QRect(320, 50, 81, 31))
        self.blackSwitch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Black.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blackSwitch.setIcon(icon)
        self.blackSwitch.setIconSize(QtCore.QSize(40, 40))
        self.blackSwitch.setChecked(True)
        self.blackSwitch.setObjectName("blackSwitch")
        self.greenSwitch = QtWidgets.QRadioButton(self.groupBox_2)
        self.greenSwitch.setGeometry(QtCore.QRect(120, 50, 81, 31))
        self.greenSwitch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("G.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.greenSwitch.setIcon(icon1)
        self.greenSwitch.setIconSize(QtCore.QSize(40, 40))
        self.greenSwitch.setObjectName("greenSwitch")
        self.redSwitch = QtWidgets.QRadioButton(self.groupBox_2)
        self.redSwitch.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.redSwitch.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("R.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redSwitch.setIcon(icon2)
        self.redSwitch.setIconSize(QtCore.QSize(40, 40))
        self.redSwitch.setObjectName("redSwitch")
        self.blueSwitch = QtWidgets.QRadioButton(self.groupBox_2)
        self.blueSwitch.setGeometry(QtCore.QRect(220, 50, 81, 31))
        self.blueSwitch.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("B.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blueSwitch.setIcon(icon3)
        self.blueSwitch.setIconSize(QtCore.QSize(40, 40))
        self.blueSwitch.setChecked(False)
        self.blueSwitch.setObjectName("blueSwitch")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 630, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.modeSwitch = QtWidgets.QToolBox(self.centralwidget)
        self.modeSwitch.setGeometry(QtCore.QRect(20, 70, 411, 351))
        self.modeSwitch.setObjectName("modeSwitch")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 411, 247))
        self.page.setObjectName("page")
        self.y_center = QtWidgets.QLineEdit(self.page)
        self.y_center.setGeometry(QtCore.QRect(80, 50, 311, 31))
        self.y_center.setObjectName("y_center")
        self.radius = QtWidgets.QLineEdit(self.page)
        self.radius.setGeometry(QtCore.QRect(80, 90, 311, 31))
        self.radius.setObjectName("radius")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.label_5.setObjectName("label_5")
        self.x_center = QtWidgets.QLineEdit(self.page)
        self.x_center.setGeometry(QtCore.QRect(80, 10, 311, 31))
        self.x_center.setObjectName("x_center")
        self.modeSwitch.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 411, 247))
        self.page_2.setObjectName("page_2")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(10, 130, 61, 31))
        self.label_15.setObjectName("label_15")
        self.cir_amount = QtWidgets.QLineEdit(self.page_2)
        self.cir_amount.setGeometry(QtCore.QRect(80, 130, 311, 31))
        self.cir_amount.setObjectName("cir_amount")
        self.max_r = QtWidgets.QLineEdit(self.page_2)
        self.max_r.setGeometry(QtCore.QRect(270, 90, 121, 31))
        self.max_r.setObjectName("max_r")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(220, 90, 51, 31))
        self.label_9.setObjectName("label_9")
        self.y_center_2 = QtWidgets.QLineEdit(self.page_2)
        self.y_center_2.setGeometry(QtCore.QRect(80, 50, 311, 31))
        self.y_center_2.setObjectName("y_center_2")
        self.x_center_2 = QtWidgets.QLineEdit(self.page_2)
        self.x_center_2.setGeometry(QtCore.QRect(80, 10, 311, 31))
        self.x_center_2.setObjectName("x_center_2")
        self.min_r = QtWidgets.QLineEdit(self.page_2)
        self.min_r.setGeometry(QtCore.QRect(80, 90, 121, 31))
        self.min_r.setObjectName("min_r")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 41, 31))
        self.label_14.setObjectName("label_14")
        self.modeSwitch.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_3.setObjectName("page_3")
        self.x_size = QtWidgets.QLineEdit(self.page_3)
        self.x_size.setGeometry(QtCore.QRect(80, 90, 121, 31))
        self.x_size.setObjectName("x_size")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.label_12.setObjectName("label_12")
        self.y_center_3 = QtWidgets.QLineEdit(self.page_3)
        self.y_center_3.setGeometry(QtCore.QRect(80, 50, 311, 31))
        self.y_center_3.setObjectName("y_center_3")
        self.x_center_3 = QtWidgets.QLineEdit(self.page_3)
        self.x_center_3.setGeometry(QtCore.QRect(80, 10, 311, 31))
        self.x_center_3.setObjectName("x_center_3")
        self.y_size = QtWidgets.QLineEdit(self.page_3)
        self.y_size.setGeometry(QtCore.QRect(270, 90, 121, 31))
        self.y_size.setObjectName("y_size")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(230, 90, 41, 31))
        self.label_13.setObjectName("label_13")
        self.modeSwitch.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 411, 247))
        self.page_4.setObjectName("page_4")
        self.y_size_2 = QtWidgets.QLineEdit(self.page_4)
        self.y_size_2.setGeometry(QtCore.QRect(270, 90, 121, 31))
        self.y_size_2.setObjectName("y_size_2")
        self.x_size_2 = QtWidgets.QLineEdit(self.page_4)
        self.x_size_2.setGeometry(QtCore.QRect(80, 90, 121, 31))
        self.x_size_2.setObjectName("x_size_2")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_16.setObjectName("label_16")
        self.y_center_4 = QtWidgets.QLineEdit(self.page_4)
        self.y_center_4.setGeometry(QtCore.QRect(80, 50, 311, 31))
        self.y_center_4.setObjectName("y_center_4")
        self.x_center_4 = QtWidgets.QLineEdit(self.page_4)
        self.x_center_4.setGeometry(QtCore.QRect(80, 10, 311, 31))
        self.x_center_4.setObjectName("x_center_4")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(220, 90, 51, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(10, 50, 61, 31))
        self.label_19.setObjectName("label_19")
        self.x_step = QtWidgets.QLineEdit(self.page_4)
        self.x_step.setGeometry(QtCore.QRect(80, 130, 121, 31))
        self.x_step.setObjectName("x_step")
        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setGeometry(QtCore.QRect(220, 130, 51, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_4)
        self.label_21.setGeometry(QtCore.QRect(10, 130, 61, 31))
        self.label_21.setObjectName("label_21")
        self.el_amount = QtWidgets.QLineEdit(self.page_4)
        self.el_amount.setGeometry(QtCore.QRect(270, 130, 121, 31))
        self.el_amount.setObjectName("el_amount")
        self.modeSwitch.addItem(self.page_4, "")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 420, 441, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 50, 441, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.graphicsView.raise_()
        self.exploreTime.raise_()
        self.groupBox.raise_()
        self.clearCanvas.raise_()
        self.algBox.raise_()
        self.groupBox_2.raise_()
        self.line.raise_()
        self.modeSwitch.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphicsView, self.algBox)
        MainWindow.setTabOrder(self.algBox, self.x_center)
        MainWindow.setTabOrder(self.x_center, self.y_center)
        MainWindow.setTabOrder(self.y_center, self.radius)
        MainWindow.setTabOrder(self.radius, self.redSwitch)
        MainWindow.setTabOrder(self.redSwitch, self.greenSwitch)
        MainWindow.setTabOrder(self.greenSwitch, self.blueSwitch)
        MainWindow.setTabOrder(self.blueSwitch, self.blackSwitch)
        MainWindow.setTabOrder(self.blackSwitch, self.drawColor)
        MainWindow.setTabOrder(self.drawColor, self.drawBg)
        MainWindow.setTabOrder(self.drawBg, self.exploreTime)
        MainWindow.setTabOrder(self.exploreTime, self.cir_amount)
        MainWindow.setTabOrder(self.cir_amount, self.clearCanvas)
        MainWindow.setTabOrder(self.clearCanvas, self.max_r)
        MainWindow.setTabOrder(self.max_r, self.y_center_2)
        MainWindow.setTabOrder(self.y_center_2, self.x_center_2)
        MainWindow.setTabOrder(self.x_center_2, self.x_size)
        MainWindow.setTabOrder(self.x_size, self.y_center_3)
        MainWindow.setTabOrder(self.y_center_3, self.x_center_3)
        MainWindow.setTabOrder(self.x_center_3, self.y_size)
        MainWindow.setTabOrder(self.y_size, self.min_r)
        MainWindow.setTabOrder(self.min_r, self.y_size_2)
        MainWindow.setTabOrder(self.y_size_2, self.x_size_2)
        MainWindow.setTabOrder(self.x_size_2, self.y_center_4)
        MainWindow.setTabOrder(self.y_center_4, self.x_center_4)
        MainWindow.setTabOrder(self.x_center_4, self.x_step)
        MainWindow.setTabOrder(self.x_step, self.el_amount)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????????? ?? ???????????????????????? ???????????????????? ???????????????????? ??????????????????????"))
        self.exploreTime.setText(_translate("MainWindow", "???????????????????????? ??????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "?????????????????? ????????????:"))
        self.drawColor.setText(_translate("MainWindow", "???????????????? ????????"))
        self.drawBg.setText(_translate("MainWindow", "???????????????? ????????"))
        self.clearCanvas.setText(_translate("MainWindow", "???????????????? ??????????"))
        self.algBox.setToolTip(_translate("MainWindow", "????????????????"))
        self.algBox.setItemText(0, _translate("MainWindow", "???????????????????????? ??????????????????"))
        self.algBox.setItemText(1, _translate("MainWindow", "?????????????????????????????? ??????????????????"))
        self.algBox.setItemText(2, _translate("MainWindow", "??????????????????"))
        self.algBox.setItemText(3, _translate("MainWindow", "?????????????? ??????????"))
        self.algBox.setItemText(4, _translate("MainWindow", "?????????????????? ??????????"))
        self.groupBox_2.setTitle(_translate("MainWindow", "???????? ????????????????????"))
        self.y_center.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.y_center.setText(_translate("MainWindow", "300"))
        self.radius.setToolTip(_translate("MainWindow", "???????????? ????????????????????"))
        self.radius.setText(_translate("MainWindow", "50"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "R"))
        self.label_5.setText(_translate("MainWindow", "Y"))
        self.x_center.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.x_center.setText(_translate("MainWindow", "300"))
        self.modeSwitch.setItemText(self.modeSwitch.indexOf(self.page), _translate("MainWindow", "????????????????????"))
        self.label_15.setText(_translate("MainWindow", "N"))
        self.cir_amount.setToolTip(_translate("MainWindow", "?????? ????????????????"))
        self.cir_amount.setText(_translate("MainWindow", "11"))
        self.max_r.setToolTip(_translate("MainWindow", "???????????????????????? ????????????"))
        self.max_r.setText(_translate("MainWindow", "150"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "Y"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>R<span style=\" font-size:7pt;\">max</span></p></body></html>"))
        self.y_center_2.setToolTip(_translate("MainWindow", "?????????? ??????????????????????"))
        self.y_center_2.setText(_translate("MainWindow", "500"))
        self.x_center_2.setToolTip(_translate("MainWindow", "?????????? ??????????????????????"))
        self.x_center_2.setText(_translate("MainWindow", "400"))
        self.min_r.setToolTip(_translate("MainWindow", "???????????????????????? ????????????"))
        self.min_r.setText(_translate("MainWindow", "50"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>R<span style=\" font-size:7pt;\">min</span></p></body></html>"))
        self.modeSwitch.setItemText(self.modeSwitch.indexOf(self.page_2), _translate("MainWindow", "???????????????????????????? ????????????????????"))
        self.x_size.setToolTip(_translate("MainWindow", "<html><head/><body><p>?????????????? ???? X</p></body></html>"))
        self.x_size.setText(_translate("MainWindow", "70"))
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_12.setText(_translate("MainWindow", "A"))
        self.y_center_3.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.y_center_3.setText(_translate("MainWindow", "350"))
        self.x_center_3.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.x_center_3.setText(_translate("MainWindow", "350"))
        self.y_size.setToolTip(_translate("MainWindow", "?????????????? ???? Y"))
        self.y_size.setText(_translate("MainWindow", "50"))
        self.label_13.setText(_translate("MainWindow", "B"))
        self.modeSwitch.setItemText(self.modeSwitch.indexOf(self.page_3), _translate("MainWindow", "????????????"))
        self.y_size_2.setToolTip(_translate("MainWindow", "?????????????? ???? Y"))
        self.y_size_2.setText(_translate("MainWindow", "30"))
        self.x_size_2.setToolTip(_translate("MainWindow", "?????????????? ???? X"))
        self.x_size_2.setText(_translate("MainWindow", "50"))
        self.label_16.setText(_translate("MainWindow", "X"))
        self.y_center_4.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.y_center_4.setText(_translate("MainWindow", "200"))
        self.x_center_4.setToolTip(_translate("MainWindow", "?????????? ????????????????????"))
        self.x_center_4.setText(_translate("MainWindow", "400"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>A<span style=\" font-size:7pt;\">min</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>B<span style=\" font-size:7pt;\">min</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Y"))
        self.x_step.setToolTip(_translate("MainWindow", "?????? ?????????????? ???? X"))
        self.x_step.setText(_translate("MainWindow", "10"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>N</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p>A<span style=\" font-size:7pt;\">??????</span></p></body></html>"))
        self.el_amount.setToolTip(_translate("MainWindow", "???????????????????? ????????????????"))
        self.el_amount.setText(_translate("MainWindow", "11"))
        self.modeSwitch.setItemText(self.modeSwitch.indexOf(self.page_4), _translate("MainWindow", "???????????????????????????? ??????????????"))
