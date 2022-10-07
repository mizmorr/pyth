#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
def texttohtml(a):    
    with open("out.html", "a") as e:
        if a.count('\n')==0:
            e.write("<pre>"+a+"</pre> <br>\n")
        else:
            for lines in a:
                e.write("<pre>" + lines + "</pre> <br>\n")
def writeintxt(a):
    out=open("out.txt","w")
    for line in a:
        out.write(line)
    out.close()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qqtask3")
        self.input = QTextEdit(self)
        self.input.move(10,10)
        self.btnhtml=QPushButton(self,text='HTML')
        self.btnhtml.move(120,10)
        self.btntxt=QPushButton(self,text='TXT')
        self.btntxt.move(120,50)
        self.btnq=QPushButton(self,text="Quit")
        self.btnq.move(10,50)
        self.setFixedSize(230,120)
        self.btnhtml.released.connect(self.btn_html)
        self.btnq.released.connect(self.quit)
        self.btntxt.released.connect(self.btn_txt)
    def btn_html(self):
        texttohtml(self.input.toPlainText())
        self.btnhtml.setEnabled(False)
        self.btnhtml.setText("Converted")
    def quit(self):
        self.close()
    def btn_txt(self):
        writeintxt(self.input.toPlainText())
        self.btntxt.setEnabled(False)
        self.btntxt.setText("Converted")

        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()