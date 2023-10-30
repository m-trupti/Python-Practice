from tkinter import *

top=Tk()
sb=Scrollbar(top)
sb.pack(side=RIGHT,fill=Y)
myList=Listbox(top,yscrollcommand=sb.set)

for line in range(30):
    myList.insert(END,"Number "+str(line))
myList.pack(side=LEFT)
    
sb.config(command=myList.yview)
top.mainloop()
