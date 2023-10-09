# IMPORT GUI MODULE
from tkinter import *


# PREPARE GUI WINDOW
root = Tk ()
root.title("28_gui_add.py")
root.geometry("320x160")

# CREATE FROM LABEL AND INPUT
Label(root, text="First No. :").pack()
Entry().pack()

#CREATE FROM LABLENAND INPUT
Lable(root, text="Second no. :").pack()
Entry().pack()

#CREATE ACTION BUTTON
Button (root, text="ADD", bg="blue", fg="white").pack()

#BUILD WINDOW COMPONENTS
root.mainloop()
