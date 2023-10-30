#Try to change the widget type configuration options to experiment with other widget types like Message,Button, Entry, CheckButton and RadioButton

#Message in Python
##from tkinter import *
##root=Tk()
##var=StringVar()
##label=Message(root,textvariable=var,relief=RAISED)
##var.set("Hey ! How are you doing?")
##label.pack()
##root.mainloop()

#Button in Python
##import tkinter
##from tkinter import messagebox
##top=tkinter.Tk()
##def helloCallBack():
##    messagebox.showinfo("Hello Python","Hello World")
##B=tkinter.Button(top,text="Hello",command=helloCallBack)
##B.pack()
##top.mainloop()


#Entry in Python
##from tkinter import *
##top=Tk()
##L1=Label(top,text="User Name")
##L1.pack(side=LEFT)
##E1=Entry(top,bd=5)
##E1.pack(side=RIGHT)
##top.mainloop()


#CheckButton in Python
##from tkinter import *
##import tkinter
##top=tkinter.Tk()
##CheckVar1=IntVar()
##CheckVar2=IntVar()
##C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
##             onvalue = 1, offvalue = 0, height=5, \
##             width = 20)
##C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
##                  height=5, onvalue = 1, offvalue = 0,\
##                 width = 20)
##C1.pack()
##C2.pack()
##top.mainloop()


#Radiobutton
##from tkinter import *
##def sel():
##    selection="You selected the option "+str(var.get())
##    label.config(text=selection)
##
##root=Tk()
##var=IntVar()
##R1=Radiobutton(root,text="Option 1",variable=var,value=1,command=sel)
##R1.pack(anchor=W)
##R2=Radiobutton(root,text="Option 2",variable=var,value=2,command=sel)
##R2.pack(anchor=W)
##R3=Radiobutton(root,text="Option 3",variable=var,value=3,command=sel)
##R3.pack(anchor=W)
##label=Label(root)
##label.pack()
##root.mainloop()
