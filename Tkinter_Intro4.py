from Tkinter import *
root = Tk()
#
#We put in two labels that ask for the name and password.
#We also put in two fields for entering information which is done using the Entry class
labelName = Label(root, text="Name", fg="red")
labelPass = Label(root, text="Password", fg="blue")
entry_1 = Entry(root)
entry_2 = Entry(root)
#We use the .grid function of organizing the widgets (objects) in the window. This allows us to
#specify the exact row and column where we want to place them.
#In order to align the text to the right, left, top or bottom, we use East, West, North, and South (E,W,N,S)
#These are put in as the value for the parameter sticky.
labelName.grid(row=0, column=0, sticky=E)
labelPass.grid(row=1, column=0, sticky=E)
#Same deal for the entry widgets
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
#Making a checkbox has its own class checkbutton.
#Making it take up both columns can be done by using the parameter columnspan
checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)

root.mainloop()