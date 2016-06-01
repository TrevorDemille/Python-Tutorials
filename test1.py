def helloWorld(String):
	print(String)
	myName = raw_input("what is my name?")
	myVar = input("enter a really low number: ")
	# 
	x = 1
	while(myVar != 0):
		if(myName != "Trevor" and myVar == 0):
			print("You typed your name wrong, bruh")
			break
		elif(myVar != 0 and x >= 5):
			myVar = input("Really? Here is a hint: its a round shape like a donut. Try again: ")
		else:
			myVar = input("Guess that number again: ")
			x = x+1
	if(myName == "Trevor" and myVar == 0):
			myName = 'Trevor is the best'
			print(myName)

helloWorld("Good Morning World")
helloWorld("Good Afternoon World")
