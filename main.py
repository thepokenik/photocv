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


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap, Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.label = QLabel(self)
        self.label.setObjectName("Capitão Biscoito")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 300, 300))
        self.label.setStyleSheet(
            """QFrame, QLabel{
                border: 2px solid #85C2FF;
                border-radius: 4px;
                color: #EBF5FF;
                padding: 2px;
                font-size:35px;
                font-weight: bold;
                text-align: center;
            }"""
        )

        self.label.setText("Capitão Biscoito")
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, pixmap.height() - 60, pixmap.width() - 20, 30)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setStyleSheet(
            """
            QProgressBar {
                background-color: #fff;
                border: 2px solid #85C2FF;
                border-radius: 10px;
                text-align: center;
                color: black;
            }
            QProgressBar:chunk {
                border-radius: 8px;
                background-color: #003366;
            }
        """
        )
        self.progress_bar.setMaximum(100)

    def set_progress(self, value):
        self.progress_bar.setValue(value)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
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
        green_img = np.zeros(self.image.shape)
        green_img[:, :, 1] = green_channel
        self.setImage(green_img)

    def redColor(self):
        green_channel = self.image[:, :, 2]
        green_img = np.zeros(self.image.shape)
        green_img[:, :, 2] = green_channel
        self.setImage(green_img)

    def blueColor(self):
        green_channel = self.image[:, :, 0]
        green_img = np.zeros(self.image.shape)
        green_img[:, :, 0] = green_channel
        self.setImage(green_img)

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
        self.zoom_at()

    def zoomOut(self):
        self.zoom -= 0.5
        if self.zoom < 1:
            self.zoom = 1
        self.label_2.setText(f"Zoom: {int(self.zoom*100)}%")
        self.zoom_at()

    def zoom_at(self, coord=None):
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
        image = cv2.imread(self.filename)
        for obj in detected_objects.to_dict(orient="records"):
            x_min, y_min, x_max, y_max = map(
                int, [obj["xmin"], obj["ymin"], obj["xmax"], obj["ymax"]]
            )
            class_id = obj["name"]

            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            label = f"{class_id}"
            cv2.putText(
                image,
                label,
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )
        self.setImage(image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pixmap = QPixmap("assets\\189447.jpg")
    splash = SplashScreen(pixmap)
    splash.show()
    i = 0

    def update_progress():
        global i
        if i <= 100:
            splash.set_progress(i)
            i += 1
            if i >= 55 and i <= 67:
                time.sleep(0.3)
        else:
            splash.finish(window)
            window.show()
            return
        QTimer.singleShot(50, update_progress)

    QTimer.singleShot(0, update_progress)

    window = MainWindow()

    sys.exit(app.exec())
