# IMPORT GUI MODULE
from Tkinter import *
 
root = Tk()
root.title("30_login")
root.iconphoto(True, photoImage(file="./favicon.png"))
root.geometry("600x200")

#create entry component varaibles
usr = StringVar()
psw = StringVar()

#create button component function
def submit():
    usr_value = usr.get()
    psw_value = psw.get()
    print(usr_value, psw_value)


    #operations in the print 
    #intVar

label(root, text="Firstname. :").pack()
Entry(textvariable=usr).pack()


label(root, text="Lastname. :").pack()
Entry(textvariable=usr).pack()


label(root, text="Date of birth. :").pack()
Entry(textvariable=usr).pack()


label(root, text="Password. :").pack()
Entry(textvariable=psw, show='*').pack()

 
label(root, text="confirm password. :").pack()
Entry(textvariable=psw, show='*').pack()


button(root, text="login", bg="blue", fg="black", command=submit).pack()


root.mainloop()
