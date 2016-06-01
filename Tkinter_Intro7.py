from Tkinter import *


class myButtons:
#__init__ is already a function of its own which is used to initialize things
	def __init__(self, master):
		frame = Frame(master, width=300, height=250)
		frame.pack()
#Im naming my widgets 'printButton' and 'quitButton', but I must say tey apply to the parameter
#self, so I use the syntax self.xyzxyzxyz 
		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT, fill=Y)
#The command parameter is calling a function I haven't described yet: printMessage
#Below, the command parameter is calling a function I don't need to define because it's built in: frame.quit
		self.quitButton = Button(frame, text="Quit", fg="red", command=frame.quit)
		self.quitButton.pack(side=LEFT, fill=Y)

	def printMessage(self):
		print("You pressed the button, A+")

#
root = Tk()
objt = myButtons(root)
root.mainloop()