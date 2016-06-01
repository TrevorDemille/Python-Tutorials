from Tkinter import *
import tkMessageBox
#
root = Tk()

tkMessageBox.showinfo("Window Title", "There are many reasons why dolphins don't speak English.")

answer = tkMessageBox.askquestion('Question 1:', 'Do you understand?')

if answer == 'yes':
	print("good for you.")
elif answer == 'no':
	print("That's too bad.")

root.mainloop()