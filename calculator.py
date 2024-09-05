from tkinter import *
from tkinter.ttk import *
window=Tk()
window.minsize(300,200)
window.maxsize(300,200)



e1=Entry(window,font=60,width=27)
e1.grid(row=0,column=0)


def insert1():
    e1.insert(END,1)
b1=Button(window,text="1",command=insert1)
b1.place(x=0,y=50)

def insert2():
    e1.insert(END,2)
b2=Button(window,text="2",command=insert2)
b2.place(x=75,y=50)

def insert3():
    e1.insert(END,3)
b3=Button(window,text="3",command=insert3)
b3.place(x=150,y=50)

def insert4():
    e1.insert(END,4)
b4=Button(window,text="4",command=insert4)
b4.place(x=0,y=75)

def insert5():
    e1.insert(END,5)
b5=Button(window,text="5",command=insert5)
b5.place(x=75,y=75)

def insert6():
    e1.insert(END,6)
b6=Button(window,text="6",command=insert6)
b6.place(x=150,y=75)

def insert7():
    e1.insert(END,7)
b7=Button(window,text="7",command=insert7)
b7.place(x=0,y=100)

def insert8():
    e1.insert(END,8)
b8=Button(window,text="8",command=insert8)
b8.place(x=75,y=100)

def insert9():
    e1.insert(END,9)
b9=Button(window,text="9",command=insert9)
b9.place(x=150,y=100)

def plus():
    e1.insert(END,"+")
bplus=Button(window,text="+",command=plus)
bplus.place(x=225,y=50)

def minus():
    e1.insert(END,"-")
bminus=Button(window,text="-",command=minus)
bminus.place(x=225,y=75)

def mult():
    e1.insert(END,"*")
bmult=Button(window,text="*",command=mult)
bmult.place(x=225,y=100)

def dot():
    e1.insert(END,".")
bdot=Button(window,text=".",command=dot)
bdot.place(x=0,y=125)

def zero():
    e1.insert(END,0)
bzero=Button(window,text="0",command=zero)
bzero.place(x=75,y=125)

def bkspace():
    a=e1.get()
    e1.delete(len(a)-1)
bspace=Button(window,text="<--",command=bkspace)
bspace.place(x=150,y=125)

def divi():
    e1.insert(END,'/')
bdivi=Button(window,text="/",command=divi)
bdivi.place(x=225,y=125)



def clear():
    a=e1.get()
    e1.delete(0,len(a))
bclear=Button(window,text="C",command=clear)
bclear.place(x=225,y=150)


def result():
    a=e1.get()
    c=eval(a)
    e1.delete(0,END)
    e1.insert(END,c)

beq=Button(window,text="=",width=36,command=result)
beq.place(x=0,y=150)























window.mainloop()