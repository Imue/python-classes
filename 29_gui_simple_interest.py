# IMPORT GUI MODULE
from Tkinter import *
 
stem = Tk()
stem.title("29_simpinterst")
stem.geometry("200x150")

label(stem, text="principal. :").pack()
Entry().pack()


label(stem, text="rate. :").pack()
Entry().pack()


label(stem, text="time. :").pack()
Entry().pack()


button(stem, text="calculate", bg="purple", fg="blue").pack()


stem.mainloop()
