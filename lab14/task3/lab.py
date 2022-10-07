from tkinter import *
import tkinter
def texttohtml(a):    
    with open("task3/out.html", "a") as e:
        if a.count('\n')==0:
            e.write("<pre>"+a+"</pre> <br>\n")
        else:
            for lines in a:
                e.write("<pre>" + lines + "</pre> <br>\n")
    mes=Message(window,text="Yes",fg='green')
    mes.place(x=130,y=115)
def writeintxt(a):
    out=open("task3/out.txt","w")
    for line in a:
        out.write(line)
    out.close()
    mes=Message(window,text="Yes",fg='green')
    mes.place(x=130,y=190)

def btnhtmlclick():
    s = enter.get()
    texttohtml(s)
def btntextclick():
    s = enter.get()
    writeintxt(s)
    
window = Tk() 
window.geometry("350x250")
frame=Frame(window)
enter=Entry(window)
enter.configure(font=('Calibri',12))
lab=Label(window)
lab2=Label(window,text="TXT converted:")
lab2.place(x=10,y=190)
lab3=Label(window,text="HTML converted: ")
lab3.place(x=10,y=115)
lab.configure(text="Введите текст: ")
lab.place(x=10,y=10)
frame.configure(background='grey')
enter.place(x=10,y=40)
frame.place(x=175,y=70)
btnhtml = Button(frame,text="HTML",command=btnhtmlclick)
btnhtml.configure(height=3,width=8)
btnhtml.grid(row=2,column=0)
btntxt=Button(frame,text="TXT",height=3,width=8,command=btntextclick)
btntxt.grid(row=6,column=3)
window.mainloop()

