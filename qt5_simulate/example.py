import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPixmap, QPaintEvent

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 720)
        self.setWindowTitle("Simple Game")

        # Fixed square size
        self.square_size = 100

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.central_layout = QVBoxLayout(self.central_widget)

        self.init_ui()
        self.setFocusPolicy(Qt.StrongFocus)

        # Initialize square position
        self.square_x = (self.width() - self.square_size) / 2
        self.square_y = (self.height() - self.square_size) / 2

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        # Set default background image path
        self.background_image = QPixmap("background.jpg")

        self.image_path = None
        self.square_image = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(10)

    def init_ui(self):
        self.create_menu_bar()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.side_layout = QVBoxLayout()
        self.side_panel = QWidget()
        self.side_panel.setFixedWidth(200)
        self.side_panel.setLayout(self.side_layout)

        self.side_image_label = QLabel()
        self.side_image_label.setFixedSize(150, 150)

        # Create an additional QLabel to display the image below the moving square
        self.bottom_image_label = QLabel()
        self.bottom_image_label.setAlignment(Qt.AlignCenter)
        self.bottom_image_label.setFixedSize(self.square_size, self.square_size)

        self.side_layout.addWidget(self.side_image_label)
        self.side_layout.addWidget(self.bottom_image_label)

        self.central_layout.addWidget(self.image_label)

    def create_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")

        change_background_action = QAction("Изменить фон", self)
        change_background_action.triggered.connect(self.change_background)
        file_menu.addAction(change_background_action)

    def change_background(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Выберите изображение для фона", "", "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)

        if file_path:
            self.background_image = QPixmap(file_path)
            self.update()
            self.update_game()

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

        # Replace with your image path
        self.image_path = "image_dron.png"

        if self.image_path:
            self.square_image = QPixmap(self.image_path)

        # Update the image in the side square
        if self.square_image:
            self.side_image_label.setPixmap(self.square_image)
            # Also set the image below the moving square
            self.bottom_image_label.setPixmap(self.square_image)

        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)

        painter.drawPixmap(0, 0, self.background_image)

        if self.square_image:
            painter.drawPixmap(int(self.square_x), int(self.square_y), self.square_image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = GameWindow()
    game_window.show()
    sys.exit(app.exec_())