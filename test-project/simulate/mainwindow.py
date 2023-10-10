# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QWidget
from PySide6.QtGui import QPixmap, QPaintEvent
from PySide6.QtCore import Qt, QEvent, QTimer, QPoint
from random import randint

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

        self.position_x = randint(self.ui.dron.width(), self.ui.map.width() - self.ui.dron.width())
        self.position_y = randint(self.ui.dron.height(), self.ui.map.height() - self.ui.dron.height())

        #show ui-elements
        self.init_UI()
        self.spawn_objects(self.position_x, self.position_y)

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
        #spinbox signal-slot
        self.ui.speed_limiter.valueChanged.connect(self.get_speed)

        self.frame_update()

    def init_UI(self):
        #map image
        self.ui.map.setPixmap(QPixmap('../images/background.png'))
        #dron image and him scaled
        self.ui.dron.setScaledContents(True)
        self.ui.dron.setPixmap(QPixmap('../images/image_dron.png'))

    def spawn_objects(self, position_x, position_y):

        self.ui.dron.move(position_x + (0.5 * self.ui.dron.width()), position_y + (0.5 * self.ui.dron.height()))
        self.ui.radius_connection.move(self.ui.dron.pos().x() - (0.25 * self.ui.radius_connection.width() ), self.ui.dron.pos().y() - (0.25 * self.ui.radius_connection.height()))

    def frame_update(self):
        #display update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(10)

    def get_speed(self):
        self.speed = self.ui.speed_limiter.value()

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

        #camera's replay
        self.ui.camera.setPixmap(self.ui.map.pixmap().copy(int(self.ui.dron.pos().x()), int(self.ui.dron.pos().y()), 200, 200))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
