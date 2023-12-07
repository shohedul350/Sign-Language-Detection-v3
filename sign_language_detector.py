# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QFileDialog
# from PyQt5.QtGui import QPixmap
# from subprocess import run

# class SignLanguageDetectorApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Sign Language Detector")
#         self.setGeometry(100, 100, 400, 300)

#         self.central_widget = QLabel(self)
#         self.central_widget.setAlignment(Qt.AlignCenter)
#         self.setCentralWidget(self.central_widget)

#         self.select_button = QPushButton("Select Image", self)
#         self.detect_button = QPushButton("Detect Sign Language", self)

#         layout = QVBoxLayout()
#         layout.addWidget(self.select_button)
#         layout.addWidget(self.detect_button)
#         layout.addWidget(self.central_widget)

#         container = QWidget(self)
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         self.select_button.clicked.connect(self.select_image)
#         self.detect_button.clicked.connect(self.detect_sign_language)

#     def select_image(self):
#         file_dialog = QFileDialog()
#         file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg;*.png;*.jpeg)")
#         if file_path:
#             self.display_image(file_path)

#     def display_image(self, file_path):
#         pixmap = QPixmap(file_path)
#         pixmap = pixmap.scaledToWidth(300)  # Adjust the width as needed
#         self.central_widget.setPixmap(pixmap)

#     def detect_sign_language(self):
#         # Replace this command with your YOLOv5 detection command
#         # Example: run(["python", "detect.py", "--source", "your_input.jpg", "--weights", "your_model.pt"])
#       run(["python3", "detect.py", "--source", "0", "--weights", "runs/train/exp6/weights/best.pt"])

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SignLanguageDetectorApp()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import cv2
from subprocess import run

class SignLanguageDetectorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign Language Detector")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QLabel(self)
        self.central_widget.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.central_widget)

        self.select_button = QPushButton("Select Image", self)
        self.detect_button = QPushButton("Detect Sign Language", self)

        layout = QVBoxLayout()
        layout.addWidget(self.select_button)
        layout.addWidget(self.detect_button)
        layout.addWidget(self.central_widget)

        container = QWidget(self)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.select_button.clicked.connect(self.select_image)
        self.detect_button.clicked.connect(self.detect_sign_language)

        # Initialize camera
        self.camera = cv2.VideoCapture(0)  # 0 corresponds to the default camera
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frames every 30 milliseconds

    def select_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg;*.png;*.jpeg)")
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaledToWidth(300)  # Adjust the width as needed
        self.central_widget.setPixmap(pixmap)

    def detect_sign_language(self):
        # Replace this command with your YOLOv5 detection command
        # Example: run(["python", "detect.py", "--source", "your_input.jpg", "--weights", "your_model.pt"])
             run(["python3", "detect.py", "--source", "0", "--weights", "runs/train/exp6/weights/best.pt"])


    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.central_widget.setPixmap(pixmap)

    def closeEvent(self, event):
        # Release the camera when the application is closed
        self.camera.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignLanguageDetectorApp()
    window.show()
    sys.exit(app.exec_())