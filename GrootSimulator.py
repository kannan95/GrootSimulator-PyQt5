

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QMovie, QIcon
from PyQt5.QtMultimedia import QSound

import os


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.setGeometry(10, 10, 475, 550)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd() + "/download.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 101, 29))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(60, 40, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 221, 401))
        self.label_2.setText("")
        self.pix = QPixmap(os.getcwd() + '/gg.jpeg')

        self.label_2.setPixmap(self.pix)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 121, 21))

        self.timer = QTimer()
        self.timer.timeout.connect(self.clear)
        self.timer.setSingleShot(True)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton.clicked.connect(self.gif)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gif(self):
        self.timer.start(2500)
        self.lineEdit.clear()
        self.audio = QSound(os.getcwd() + '/groot.wav')
        self.audio.play()

        self.pix1 = QMovie('movie.gif')
        self.label_3.setMovie(self.pix1)
        self.pix1.start()
        self.label_3.adjustSize()

    def clear(self):
        self.label_3.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Message:"))


if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Groot Simulator")
    ui = Ui_MainWindow()

    MainWindow.show()
    sys.exit(app.exec_())
