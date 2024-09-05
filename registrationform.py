from tkinter import *
# from tkinter.ttk import *
# from tkinter import messagebox

window=Tk()
# title=window.text="ALAYAM"
e1=Entry(window,font=('Arial',22))
h1=Label(window,text="NAME :",font=22)
h1.grid(row=0,column=0)
e1.grid(row=0,column=1)

# e1.Entry(window)


e2=Entry(window,font=('Arial',22))
h2=Label(window,text="AGE :",font=22)
h2.grid(row=1,column=0)
e2.grid(row=1,column=1)


e3=Entry(window,font=('Arial',22))
h3=Label(window,text="ADDRESS :",font=22)
h3.grid(row=2,column=0)
e3.grid(row=2,column=1)


h4=Label(window,text="GENDER :",font=22)
h4.grid(row=3,column=0)

rad1=Radiobutton(window,text='Male',value=1,font=18)
rad2=Radiobutton(window,text="Female",value=2,font=18)
rad1.place(x=120,y=110)
rad2.place(x=200,y=110)






from tkinter import messagebox

def msg():
    messagebox.showinfo("Look Carefully","Mind Your Business")
btn=Button(window,text='submit',font=18,command=msg)
btn.place(x=400,y=150)

window.mainloop()