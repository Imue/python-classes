from tkinter import *

root = Tk()
root.title("27_gui.py")
root.geometry("400x400" )

Label = Label(root,text="Username t")
Label.pack()

textbox = Entry()
textbox.pack()


btn1 = button(root, text="OK")
btn1.pack()

btn2  - Button(root, text="cancel")
btn2.pack()

root.mainloop()              
