from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *
keys = open("keys.txt","r")
vals = open("vals.txt","r")
lkeys = keys.readlines()
lvals=vals.readlines()
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count=0
        self.i=randint(0,len(list(d.keys()))-1)
        self.setWindowTitle("Qqtask2")        
        self.inputword=QLineEdit(self)
        self.button=QPushButton('Moved',self,text='try')
        self.labword=QLabel('Moved',self,text="word:  "+list(d.keys())[self.i])
        self.labword.setFixedWidth(200)
        self.button.move(50,100)
        self.labattmpts=QLabel('Moved',self,text='attempt: '+str(self.count))
        self.btnsurrender=QPushButton('Moved',self,text='surrender')
        self.btnsurrender.move(50,160)
        self.inputword.move(260,40)
        self.labattmpts.setFixedWidth(200)
        self.labtransl=QLabel('Moved',self,text="translate:")
        self.setFixedSize(QSize(400,300))
        self.labword.move(10,40)
        self.labtransl.move(180,40)
        self.labattmpts.move(180,90)
        self.surrendlab=QLabel(self)
        self.button.released.connect(self.try_translate)
        self.btnsurrender.released.connect(self.give_up)
        self.surrendlab.setFixedWidth(200)
    def try_translate(self):
        word=self.inputword.text().strip().lower()
        if word.isspace()==False:
            if word==d[list(d.keys())[self.i]]:
                self.btnsurrender.setEnabled(False)
                self.labattmpts.setFixedWidth(125)
                self.labattmpts.setStyleSheet("background-color: light green;"
                                              "border: 1px solid green;")
                self.labattmpts.setText("you are correct!")
            else:
                if self.count==2:
                    self.button.setEnabled(False)
                    self.labattmpts.setText("attempt: was last")
                else:
                    self.count+=1
                    self.labattmpts.setText("attempt: "+str(self.count))
        else:
            print('space')
    def give_up(self):
        self.surrendlab.setText("word - "+d[list(d.keys())[self.i]])
        self.surrendlab.move(180,150)
        self.button.setEnabled(False)
        self.labattmpts.setText("you gave up!")        
def cleart(a): 
    return (a.replace("\t",' '))
def strformatter(a):
    b=list()
    for elem in a:
        if elem.count(' ')==0:
            b.append(elem)
        else:
            b+=([e for e in elem.replace(',','').split(' ') if e!=''])
    return b
d={}
for i in range(len(lkeys)):
    postkeys=strformatter(list(map(lambda x: cleart(x),lkeys[i].rstrip().split(' '))))
    postvals=list(map(lambda x: x.rstrip().lstrip(), [val for val in lvals[i].split(' ') if val!='\n'and val!='']))
    for j in range(len(postkeys)):
        d[postkeys[j]]=postvals[j]
        
     
     
    
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
