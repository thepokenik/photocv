# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSplitter,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet("")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(120, 50, 1151, 621))
        self.label.setStyleSheet("border: 1px solid #000;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(1180, 60, 81, 78))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color:#fff;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 10, 101, 31))
        self.label_3.setStyleSheet('font: 9pt "Roboto";')
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1110, 10, 158, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.layoutWidget1)
        self.pushButton_11.setObjectName("pushButton_11")

        self.horizontalLayout.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName("pushButton_10")

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 600, 101, 61))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.pushButton_9 = QPushButton(self.layoutWidget2)
        self.pushButton_9.setObjectName("pushButton_9")

        self.verticalLayout_4.addWidget(self.pushButton_9)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 470, 101, 121))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.pushButton_4 = QPushButton(self.layoutWidget3)
        self.pushButton_4.setObjectName("pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget3)
        self.pushButton_5.setObjectName("pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget3)
        self.pushButton_6.setObjectName("pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 350, 101, 111))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.pushButton_3 = QPushButton(self.layoutWidget4)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.lineEdit = QLineEdit(self.layoutWidget4)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget4)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setGeometry(QRect(12, 58, 101, 53))
        self.splitter.setOrientation(Qt.Vertical)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.splitter.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.layoutWidget4.raise_()
        self.label_3.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", "+", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Zoom:", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:16pt; font-weight:700;">PhotoCV</span></p></body></html>',
                None,
            )
        )
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", "_", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", "X", None))
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Model:</p></body></html>',
                None,
            )
        )
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", "Detect", None)
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Channel:</p></body></html>',
                None,
            )
        )
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", "Red", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Green", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", "Blue", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Size:</p></body></html>',
                None,
            )
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Resize", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Width...", None)
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Height...", None)
        )
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Open", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Save as", None)
        )

    # retranslateUi
