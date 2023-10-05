import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPixmap, QPaintEvent

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Simple Game")

        self.central_layout = QHBoxLayout(self)
        self.image_label = QLabel(self)
        self.background_label = QLabel(self)  # Создаем QLabel для фона
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # Устанавливаем размер фона равным размеру окна

        self.central_layout.addWidget(self.image_label)

        self.init_ui()
        self.setFocusPolicy(Qt.StrongFocus)

        self.square_size = 100
        self.square_x = (self.width() - self.square_size) / 2
        self.square_y = (self.height() - self.square_size) / 2

        self.image_x = 0

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(10)

    def init_ui(self):
        self.background_image = QPixmap("background.png")

        self.change_background_button = QPushButton("Изменить фон", self)
        self.change_background_button.clicked.connect(self.change_background)

        self.side_panel = QWidget()
        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_panel.setFixedWidth(200)
        self.side_image_label = QLabel()
        self.side_image_label.setFixedSize(150, 150)
        self.side_layout.addWidget(self.side_image_label)
        self.central_layout.addWidget(self.side_panel)
        self.central_layout.addWidget(self.background_label)

    def change_background(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Выберите изображение для фона", "", "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)

        if file_path:
            self.background_image = QPixmap(file_path)
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
            self.square_y -= step
        if self.move_down:
            self.square_y += step
        if self.move_left:
            self.square_x -= step
        if self.move_right:
            self.square_x += step

        self.square_x = max(0, min(self.square_x, self.width() - self.square_size))
        self.square_y = max(0, min(self.square_y, self.height() - self.square_size))

        self.image_x += step
        self.side_image_label.setPixmap(self.background_image.copy(int(self.square_x), int(self.square_y), 150, 150))

        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)

        # Рисуем фон
        painter.drawPixmap(0, 0, self.background_image)

        # Рисуем квадрат в центре
        painter.fillRect(int(self.square_x), int(self.square_y), self.square_size, self.square_size, Qt.red)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = GameWindow()
    game_window.show()
    sys.exit(app.exec_())