from random import randint
import tkinter
keys = open("keys.txt","r")
vals = open("vals.txt","r")
lkeys = keys.readlines()
lvals=vals.readlines()

def btnclick():
    if counter.get()<3:
        wd=word.get().rstrip().lstrip().lower()
        if wd==d[list(d.keys())[i]]:
            mes.configure(text="Верно",fg='green')
            btn.configure(bg="green")
            btn.configure(state='disabled')
            counter.set(0)
            
        else:
            btn.configure(bg="red")
            mes.configure(text="Неверно!",fg='red')
            counter.set(counter.get()+1)
        mes.place(x=205, y = 160)
    else:
        mes.configure(text="Ты проиграл!",fg='black',bg='red')
        mes.place(x=205, y = 160)
        btn.configure(state='disabled')
def surrender():
    btn.configure(state='disabled')
    mes.configure(text="Слово - "+str(d[list(d.keys())[i]]),width=250,fg='red')
    mes.place(x=170, y = 160)
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
        

window=tkinter.Tk(className="task")
window.geometry("500x250")
mes = tkinter.Message(window,text="Верно!",width=100,fg='green',font=('Arial,15'))
i=randint(0,len(list(d.keys()))-1)
var = tkinter.StringVar()
var="Слово: "+list(d.keys())[i]
rightness="test"
lab=tkinter.Label(text=var, font=('Arial', 15),width=50,height=3)
lab.pack()
frame = tkinter.Frame(window)
frame.pack()
btn=tkinter.Button(frame,command=btnclick,width=10,height=2,text="try",font=('Arial',15, 'bold'))
btn.pack(side=tkinter.TOP)
word =tkinter.Entry(window,width=20)
word.place(x=325,y=112)
lab2=tkinter.Label(text="Перевод: ", font=('Arial', 15,'italic'))
lab2.place(x=325,y=70)
counter=tkinter.IntVar()
counter.set(0)
lab3=tkinter.Label(window,textvariable=counter,width=1,font=('Arial', 11))
lab3.place(x=150,y=100)
lab4=tkinter.Label(window,text ='Попытка: ',font=('Arial', 11))
lab4.place(x=70, y =100)
btnsur=tkinter.Button(window,command=surrender,width=5,height=2,text="сдаюсь",font=('Arial',13, 'bold'),bg='red')
btnsur.place(x=0,y=0)
window.mainloop()
