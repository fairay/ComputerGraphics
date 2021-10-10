# Лабораторная работа №4

import sys
from my_gui import *

app, application = None, None


class MainWin(QtWidgets.QMainWindow):
    ui = None

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.ui.draw_point(event.pos().x(), event.pos().y(), False)
        elif event.button() == Qt.RightButton:
            self.ui.draw_point(event.pos().x(), event.pos().y(), True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.ui.fill_mode_on()
        elif event.key() == Qt.Key_Delete:
            self.ui.clear_scene()

    def __init__(self):
        super().__init__()
        self.ui = GuiMainWin()
        self.ui.setupUi(self)
        self.setAnimated(True)
        self.setUpdatesEnabled(True)


def main():
    global app, application
    app = QtWidgets.QApplication([])
    application = MainWin()
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
