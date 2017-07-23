from Groot_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSound
import os


class groot(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.clear)
        self.timer.setSingleShot(True)
        self.pushButton.clicked.connect(self.gif)

    def gif(self):
        self.timer.start(2500)
        self.lineEdit.clear()
        # self.audio = QSound(':/files/groot.wav')
        # self.audio.play()

        self.pix1 = QMovie('GrootGif.gif')
        self.label_3.setMovie(self.pix1)
        self.pix1.start()
        self.label_3.setScaledContents(True)

    def clear(self):
        self.label_3.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gr = groot()
    gr.show()
    app.exec_()
