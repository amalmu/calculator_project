from tkinter import *


window=Tk()
window.geometry('500x400')#to size the window
# window.maxsize(500,500)#set max size
# window.minsize(300,500)#minsize
window.title("HELOO GUYZ")#to change the title
lbl=Label(window,text='Assalamu Alaikum')
lbl.grid(row=3,column=5)

# lb=Label(window,text='Assalamu')
# lb.grid(row=6,column=9)

# e1=Entry(window)
# e1.grid(row=9,column=9)
e=Entry(window)
e.grid(row=8,column=10)
#to entry something#

# e=Entry(window,state=DISABLED)
# e.grid(row=8,column=10)
#to disable entry of entri box#


def en():
    d=e.get()
    print(d)



window.mainloop()#should be close tkinter window with this command