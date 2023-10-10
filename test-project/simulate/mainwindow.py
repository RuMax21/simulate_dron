# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QWidget
from PySide6.QtGui import QPixmap, QPaintEvent
from PySide6.QtCore import Qt, QEvent, QTimer, QPoint
import random

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        #Values
        self.speed = 2
        #bool values for moving
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        #menubar actions
        self.ui.action_background.triggered.connect(self.change_background)
        self.ui.action_exit.triggered.connect(self.close)

        #display update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(10)

    def init_UI(self):
        #start image
        self.ui.map.setPixmap(QPixmap('../images/background.png'))

        self.ui.dron.setScaledContents(True)
        self.ui.dron.setPixmap(QPixmap('../images/image_dron.png'))

    def change_background(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select image for map", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)

        if file_path:
            self.ui.map.setPixmap(QPixmap(file_path))
            self.update()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.move_up = True
        elif event.key() == Qt.Key_S:
            self.move_down = True
        elif event.key() == Qt.Key_A:
            self.move_left = True
        elif event.key() == Qt.Key_D:
            self.move_right = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.move_up = False
        elif event.key() == Qt.Key_S:
            self.move_down = False
        elif event.key() == Qt.Key_A:
            self.move_left = False
        elif event.key() == Qt.Key_D:
            self.move_right = False

    def update_game(self):
        if self.move_up:
            self.ui.dron.move(self.ui.dron.pos() + QPoint(0, -self.speed))
        if self.move_down:
            self.ui.dron.move(self.ui.dron.pos() + QPoint(0, self.speed))
        if self.move_left:
            self.ui.dron.move(self.ui.dron.pos() + QPoint(-self.speed, 0))
        if self.move_right:
            self.ui.dron.move(self.ui.dron.pos() + QPoint(self.speed, 0))

        self.ui.camera.setPixmap(self.ui.map.pixmap().copy(int(self.ui.dron.pos().x()), int(self.ui.dron.pos().y()), 200, 200))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
