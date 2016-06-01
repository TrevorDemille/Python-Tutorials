from Tkinter import *
root = Tk()
#
#Now, we're making two functions to recognize right and left clicks which are 
#dependant on some event we will define later as right and left clicking, obviously
def leftClick(event):
	print("You left clicked, congrats boy-o!")
def rightClick(event):
	print("You right clicked, you must be super cool..")
#We make frames in the window aka areas of organization for placing shit later on.
#I can define the size of the frame by the pixel count in width and height too.
frame = Frame(root, width=300, height=250)
#We use .bind to decide rightclick <Button-3> or left click <Button-1> or middle click <Button-2>
#We then call the necessary function
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.pack()
#
root.mainloop()