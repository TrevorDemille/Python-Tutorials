def add(num1, num2):
	return num1 + num2
#
def sub(num1, num2):
	return num1 - num2
#
def mult(num1, num2):
	return num1*num2
#
def div(num1, num2):
	return num1/num2
#
def exp(num1, num2):
	return num1**num2


def main():
	operation = raw_input("What do you want to do (+,-,*,/,^):")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '^'):
		print("Invalid Operation")
	else:
		val1 = int(input("Enter num1: "))
		val2 = int(input("Enter num2: "))
		if(operation == '+'):
			print(add(val1, val2))
		elif(operation == '-'):
			print(sub(val1, val2))
		elif(operation == '*'):
			print(mult(val1, val2))
		elif(operation == '/'):
			print(div(val1, val2))
		else:
			print(exp(val1, val2))
#
main()