import sys
import cv2
import numpy as np
import torch
import time
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from uimain import Ui_MainWindow
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class SplashScreen(QWidget):
    def __init__(self, pixmap):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        layout = QVBoxLayout(self)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)

        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)
        self.progressBar.setMinimum(0)
        self.progressBar.setStyleSheet(
            """
            QProgressBar {
                background-color: rgba(255, 255, 255, 0);
                border: 2px solid rgb(200, 200, 200);
                border-radius: 10px;
                text-align: center;
                font-size: 15px;
                font-weight: bold;
                color: black;
            }
            QProgressBar:chunk {
                border-radius: 8px;
                background-color: #85C2FF;
            }
        """
        )
        self.progressBar.setMaximum(100)

    def set_progress(self, value):
        self.progressBar.setValue(value)


def centerWindow(window):
    available_geometry = QGuiApplication.screens()[0].availableGeometry()
    window_rect = window.geometry()
    x = (available_geometry.width() - window_rect.width()) // 2
    y = (available_geometry.height() - window_rect.height()) // 2
    window.move(x, y)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.viewer = QLabel(self)
        self.viewer.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.viewer.setMinimumSize(QSize(800, 500))
        self.setupUi(self)
        self.pushButton.pressed.connect(self.loadImage)
        self.pushButton_5.pressed.connect(self.greenColor)
        self.pushButton_4.pressed.connect(self.redColor)
        self.pushButton_6.pressed.connect(self.blueColor)

        self.pushButton_7.pressed.connect(self.zoomIn)
        self.pushButton_8.pressed.connect(self.zoomOut)

        self.pushButton_9.pressed.connect(self.inferenceImage)

        self.pushButton_2.pressed.connect(self.saveImage)

        self.pushButton_3.pressed.connect(self.resizeImage)

        self.model = torch.hub.load("ultralytics/yolov5", "yolov5x")

        self.lineEdit.textChanged.connect(self.sizeValues)
        self.lineEdit_2.textChanged.connect(self.sizeValues)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

        self.zoom = 1

        self.filename = None
        self.tmp = None

    def updateLabel(self):
        self.label.setText("Button clicked!")

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*)")[0]
        self.image = cv2.imread(self.filename)
        self.setImage(self.image)

    def setImage(self, image):
        self.tmp = image
        image = cv2.resize(image, (1151, 650))
        if image.dtype != "uint8":
            image = cv2.convertScaleAbs(image)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888,
        )
        self.label.setPixmap(QPixmap.fromImage(image))

    def greenColor(self):
        green_channel = self.image[:, :, 1]
        image = np.zeros(self.image.shape)
        image[:, :, 1] = green_channel
        self.setImage(image)

    def redColor(self):
        red_channel = self.image[:, :, 2]
        image = np.zeros(self.image.shape)
        image[:, :, 2] = red_channel
        self.setImage(image)

    def blueColor(self):
        blue_channel = self.image[:, :, 0]
        image = np.zeros(self.image.shape)
        image[:, :, 0] = blue_channel
        self.setImage(image)

    def sizeValues(self):
        self.input = QLineEdit()
        widthValue = int(self.lineEdit.text())
        heightValue = int(self.lineEdit_2.text())
        return widthValue, heightValue

    def resizeImage(self):
        resized = cv2.resize(self.image, self.sizeValues())
        self.setImage(resized)

    def saveImage(self):
        filename, _ = QFileDialog.getSaveFileName(
            filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)"
        )
        if filename:
            cv2.imwrite(filename, self.tmp)
            print("Image saved as:", filename)

    def zoomIn(self):
        self.zoom += 0.5
        self.label_2.setText(f"Zoom: {int(self.zoom*100)}%")
        self.zoomAt()

    def zoomOut(self):
        self.zoom -= 0.5
        if self.zoom < 1:
            self.zoom = 1
        self.label_2.setText(f"Zoom: {int(self.zoom*100)}%")
        self.zoomAt()

    def zoomAt(self, coord=None):
        h, w, _ = [self.zoom * i for i in self.image.shape]

        if coord is None:
            cx, cy = w / 2, h / 2
        else:
            cx, cy = [self.zoom * c for c in coord]

        img = cv2.resize(self.image, (0, 0), fx=self.zoom, fy=self.zoom)
        img = img[
            int(round(cy - h / self.zoom * 0.5)) : int(round(cy + h / self.zoom * 0.5)),
            int(round(cx - w / self.zoom * 0.5)) : int(round(cx + w / self.zoom * 0.5)),
            :,
        ]
        self.setImage(img)

    def inferenceImage(self):
        results = self.model(self.image)
        detected_objects = results.pandas().xyxy[0]
        print(detected_objects)
        for obj in detected_objects.to_dict(orient="records"):
            x_min, y_min, x_max, y_max = map(
                int, [obj["xmin"], obj["ymin"], obj["xmax"], obj["ymax"]]
            )
            class_id = obj["name"]

            cv2.rectangle(self.image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            label = f"{class_id}"
            cv2.putText(
                self.image,
                label,
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )
        self.setImage(self.image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    pixmap = QPixmap("assets/logo.png")
    pixmap = pixmap.scaled(250, 250)
    splash = SplashScreen(pixmap)
    splash.show()
    centerWindow(splash)
    i = 0

    def update_progress():
        global i
        if i <= 100:
            splash.set_progress(i)
            i += 1
            if i >= 55 and i <= 67:
                time.sleep(0.3)
        else:
            splash.close()
            window.show()
            centerWindow(window)
            return
        QTimer.singleShot(50, update_progress)

    QTimer.singleShot(0, update_progress)

    window = MainWindow()

    sys.exit(app.exec())
