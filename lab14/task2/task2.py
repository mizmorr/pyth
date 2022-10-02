import tkinter
keys = open("task2/keys.txt","r")
vals = open("task2/vals.txt","r")
lkeys = keys.readlines()
lvals=vals.readlines()
def btnclick():
    mes.pack()
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
        

window=tkinter.Tk()
mes = tkinter.Message(window,text="message",width=50)


frame = tkinter.Frame(window)
frame.pack()
btn=tkinter.Button(frame,command=btnclick)
btn.pack()
window.mainloop()