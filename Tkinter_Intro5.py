from Tkinter import *
root = Tk()
#We make a function that we want to connect to a widget that just prints to the command line
def printName():
	print("Haha $0.00")
#Now we use the command parameter to tell the widget what to do when it is interacted with, aka clicked.
button1 = Button(root, text="Print Ty's bank statement", fg="red", command=printName)
button1.grid(row=0)
#
#We give this function a parameter aka event, which will specify what must be done to call the function
def printAgain(event):
	print("Roasted")
#We're doing the same thing, only this time we use the .bind function to decide which event we
#care about, and what to do when it happens. <Button-1> means left click.
button2 = Button(root, text="Print Ty's status", fg="blue")
button2.bind("<Button-1>", printAgain)
button2.grid(row=1)

root.mainloop()