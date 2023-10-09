# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QPaintEvent
from PySide6.QtCore import Qt, QEvent, QTimer

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
#        self.init_UI()

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        #menubar actions
        self.ui.action_background.triggered.connect(self.change_background)
        self.ui.action_exit.triggered.connect(self.close)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(10)
#        self.ui.map.setPixmap(QPixmap('/home/max/Рабочий стол/test-project/images/background.png'))

    def change_background(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select image for map", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)

        if file_path:
            self.ui.map.setPixmap(QPixmap(file_path))
            self.update()


    def keyPressEvent(self, event):
        step = 5
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
        step = 5

        if self.move_up:
            self.ui.dron.y -= step
        if self.move_down:
            self.ui.dron.y += step
        if self.move_left:
            self.ui.dron.x -= step
        if self.move_right:
            self.ui.dron.x += step

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
