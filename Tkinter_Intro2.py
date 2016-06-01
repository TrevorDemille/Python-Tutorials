from Tkinter import *
#Root creates the blank window with the Tk class. Root is an object
root = Tk()
#We can split the window into different areas within which thing can be placed. These are called frames
#We use .pack to just 'pack' the frames into the window however it can be specificed as a parameter
#just where to arrange the frames.
topFrame = Frame(root)
topFrame.pack(side=TOP)
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)
#
#Creating buttons uses the class 'Button' which takes parameters asking where, what, and what color?
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(botFrame, text="Button 4", fg="purple")
#Next, we actually tell the buttons to be packed into the window
#We tell .pack to put the buttons to the right or left of each ther inside the frames, otherwise
#.pack will stack the buttons in a column
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
#Run the window (root) as a loop of the main class, or else it will only display for like 1/1000 of a sec
root.mainloop()