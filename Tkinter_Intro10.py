from Tkinter import *
import tkMessageBox
#
root = Tk()
#Make a canvas, like a frame, within the indow which allows for the drawing of shapes and colors.
myCanvas = Canvas(root, width=200, height=100)
myCanvas.pack()
#Make a black line by telling it starting x, and y, then ending x, and y
blackline = myCanvas.create_line(0, 0, 200, 50)
#Make a red rectangle by telling it top left point x and y, then width(150) and height(75)
redbox = myCanvas.create_rectangle(50, 50, 150, 75, fill="red")

#Ask to delete things
answer1 = tkMessageBox.askquestion("First", "Delete the red box?")

if answer1 == 'yes':
	myCanvas.delete(redbox)
	print("Awh..")
elif answer1 == 'no':
	print("Good choice, we like red boxes")
#
answer2 = tkMessageBox.askquestion("Second", "Delete the black line?")
if answer2 == 'yes':
	myCanvas.delete(blackline)
	print("Ha! gottem.")
else:
	print("Fair enough")

root.mainloop()