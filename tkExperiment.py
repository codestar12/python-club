from Tkinter import *

root = Tk()

for i in range(10):
    w = Label(root, text="Hello, world!" + str(i))
    w.pack()
    root.update_idletasks()
    

