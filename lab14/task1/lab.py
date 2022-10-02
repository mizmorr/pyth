import tkinter
def click():
    pre=entry.get()
    
    lab.config(text=((int(pre)-32)/1.8))
def q():
    window.quit()
window=tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()
var=tkinter.StringVar()

entry=tkinter.Entry(frame,textvariable=var)
entry.pack()
button =tkinter.Button(frame,text="Convert",command=click)
button.pack()
qu=tkinter.Button(frame,text="Quit",command=q)
qu.pack()
lab=tkinter.Label(window)
lab.pack()
window.mainloop()