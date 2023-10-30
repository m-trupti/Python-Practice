#CheckButton in Python
from tkinter import *
import tkinter
top=tkinter.Tk()
top.geometry("300x300")
var = StringVar()
CheckVar1=IntVar()
CheckVar2=IntVar()
C1 = Checkbutton(top, text = "Male", variable = CheckVar1, \
             onvalue = 1, offvalue = 0, height=5, \
             width = 20)
C2 = Checkbutton(top, text = "Female", variable = CheckVar2, \
                  height=5, onvalue = 1, offvalue = 0,\
                 width = 20)
def clickMe():
    if CheckVar1.get():
        var.set("You selected Male")
    if CheckVar2.get():
         var.set("You selected Female")

label = Label(top, textvariable=var, relief=RAISED)
C1.pack()
C2.pack()
B=tkinter.Button(top,text="Show",command=clickMe)
B.pack()
label.pack()
top.mainloop()
