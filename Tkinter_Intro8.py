from Tkinter import *
#Dropdown menus!

def doNothing():
	print("Haha, definitey not cool")
def alsoNothing():
	print("Bout as fresh as month old milk in the summer")
def Nada():
	print("Soft af")
def Copy():
	print("No copying for you, fool!")
def Cut():
	print("Do I look like I have any scissors?")
def Paste():
	print("Don't eat the paste, lil Timmy!")
#This function could do things like save or copy, or cut etc
#We make our window first
root = Tk()
frame = Frame(root, width=300, height=250)
#Defne a menu using the menu class and put it in root
#Then, I configure the menu, which tells python to put the menu at the top and such.
bigMenu = Menu(root)
root.config(menu=bigMenu)
#Submenu don't go in root, they go in the menu they are a part of. Also, instead of configuring,
#Now, we must cascade the menus inside whichever the parent was
subMenu1 = Menu(bigMenu)
bigMenu.add_cascade(label="Ty-Lucas", menu=subMenu1)
subMenu2 = Menu(bigMenu)
bigMenu.add_cascade(label="Edit", menu=subMenu2)
#Now, I'm making actual things to click on in the submenu. They are going to do whichever function 
#is tied to them through command
subMenu1.add_command(label="Coolness", command=doNothing)
subMenu1.add_command(label="Freshness", command=alsoNothing)
subMenu1.add_command(label="Hardness", command=Nada)
subMenu1.add_separator()
subMenu1.add_command(label="Exit Window", command=frame.quit)
#
subMenu2.add_command(label="Copy", command=Copy)
subMenu2.add_command(label="Cut", command=Cut)
subMenu2.add_command(label="Paste", command=Paste)

# ***** ToolBar Time *****

toolbar = Frame(root, bg="blue")

insert1 = Button(toolbar, text="Insert Image", command=doNothing)
insert1.pack(side=LEFT, padx=5, pady=5)
insert2 = Button(toolbar, text="Print Image", command=Cut)
insert2.pack(side=LEFT, padx=5, pady=5)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

#We make a label, plae it in root, give it a text, then set border to 1 (true), give it a sunken depth of field, 
#and anchor it to the left side of the screen
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()