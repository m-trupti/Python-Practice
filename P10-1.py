#Try to configure the widget with various options like : bg="red",family="times",size=18

import  tkinter
from tkinter import *
root=Tk()
o=Canvas(root,bg="red",width=500,height=500)
o.pack()
n=Label(root,text="Hello World")
n.pack()
root.mainloop()
