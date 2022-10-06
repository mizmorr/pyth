from tkinter import *
from tkinter.ttk import Combobox
from math import pi,pow  

def solve():
    s=entrad.get().strip()
    if s=="" or s.isdigit()==False:
        mes.configure(text='bad format')
    else:
        resint=pi*pow(int(s),3)*(4/3)
        resstr=StringVar()
        resstr=resint
        res.configure(text=resstr)
        mes.configure(text="")

def texttohtml(a):    
    with open("out.html", "a") as e:
        e.write("<pre>" +"Результат - "+str(a) + "</pre> <br>\n")
    
def writeintxt(a):
    out=open("out.txt","w")
    out.write("res: "+str(a))
    out.close()

def save():
    s=res.cget("text")
    if str(s).isspace()==False:
        if combo.get()=="HTML":
            texttohtml(s)
        else:
            writeintxt(s)
        mes=Message(window,text='saved',fg='green',width=100)
        mes.place(x=80,y=340)
window=Tk()
mes=Message(window,fg='red',width=100)
mes.place(x=295,y=110)
lab1=Label(text="Программа для вычисления объема сферы",font=('Times New Roman',12,'bold'))
lab1.place(x=100,y=20)
lab2 = Label(text="Введите радиус: ", font=('Times New Roman',14))
lab2.place(x=40,y=80)
lab3 = Label(text="Результат вычислений: ", font=('Times New Roman',14))
lab3.place(x=40,y=160)
btnsolve=Button(text="Вычислить",font=('Times New Roman',12),command=solve)
btnsolve.configure(height=2,width=15)
btnsolve.place(x=180,y=225)
entrad = Entry(font=('Times New Roman',14),width=18)
entrad.place(x=270,y=80)
res=Label(font=('Times New Roman',14),width=18)
res.place(x=270,y=160)
btnsave = Button(text='Сохранить',height=1,width=14,command=save)
btnsave.place(x=40,y=300)
combo=Combobox()
combo['values']=('HTML','Текст')
combo.current(0)
combo.configure(height=100,width=19)
combo.place(x=270,y=300)
window.geometry("500x500")
window.mainloop()
