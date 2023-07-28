# -- coding: utf-8 --

################################################################################
## Form generated from reading UI file 'mainFwiJha.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
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
        self.label.setGeometry(QRect(120, 10, 1151, 650))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 170, 101, 41))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 101, 61))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 580, 101, 86))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 80, 101, 82))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(1180, 20, 77, 78))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.layoutWidget3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget3)
        self.pushButton_8.setObjectName("pushButton_8")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color:#fff;")

        self.verticalLayout_3.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton.clicked.connect(self.label.update)
        self.lineEdit.textChanged.connect(MainWindow.show)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", "Detect", None)
        )
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "Load", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Save", None)
        )
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", "Red", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Green", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", "Blue", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Resize", None)
        )
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Width...", None)
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Height...", None)
        )
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", "+", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", "-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Zoom:", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", "Main", None))

    # retranslateUi
