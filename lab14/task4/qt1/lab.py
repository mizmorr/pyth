#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qqtask1")
        self.input = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        self.label=QLabel()
        self.buttonConvert=QPushButton(text="Convert")
        self.buttonConvert.released.connect(self.Convert)
        self.buttonQ=QPushButton(text="Quit")
        self.buttonQ.released.connect(self.Q)
        self.label.setStyleSheet("border :1px solid black;"
                                   "border-top-left-radius :10px;"
                                   " border-top-right-radius : 10px; "
                                   "border-bottom-left-radius : 10px; "
                                   "border-bottom-right-radius : 10px")
        layout.addWidget(self.label)
        layout.addWidget(self.buttonConvert)
        layout.addWidget(self.buttonQ)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setFixedSize(QSize(250,150))
    def Convert(self):
        s=self.input.text().strip()
        self.label.setText(str((int(s)-32)/1.8))
    def Q(self):
        window.close()
        
        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()