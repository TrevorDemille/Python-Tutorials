from Tkinter import *
root = Tk()
#Making widgets with the label class. I can change the background color (bg) and foreground color (fg)
#If I don't put any parameters for .pack for a label, it will stay the same size as the parent window is expanded
#If I put fill into .pack, and tell it which direction (X), it will resize with the window
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="white")
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()