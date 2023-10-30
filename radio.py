from tkinter import *
def selection():
    selection="You selected the option "+str(radio.get())
    label.config(text=selection)

root=Tk()
root.geometry("300x150")
radio=IntVar()
lb1=Label(text="Favourite Programming Language ?")
lb1.pack()
R1=Radiobutton(root,text="C",variable=radio,value=1,command=selection)
R1.pack(anchor=W)
R2=Radiobutton(root,text="C++",variable=radio,value=2,command=selection)
R2.pack(anchor=W)
R3=Radiobutton(root,text="Java",variable=radio,value=3,command=selection)
R3.pack(anchor=W)
label=Label(root)
label.pack()
root.mainloop()
