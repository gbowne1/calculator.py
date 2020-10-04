while True:
	print ("If you want to add two numbers, please type 'add'")
	print ("If you want to subtract two numbers, please type 'subtract'")
	print ("If you want to divide two numbers, please type 'divide'")
	print ("If you want to multiply two numbers, please type 'multiply'")
	print ("If you want to end the program, please type 'quit'")
	
def add(x, y):
        return x + y

def subtract (x, y):
        return x - y
        
def multiply(x, y):
        return x * y

def divide (x, y):
        return x / y
	
choice = input("Enter choice(1/2/3/4: ")
	
if choice == '1':
        print(num1, "+", num2,"=", add(num1,num2))

elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))
        
elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))

def user_input = "add":
		num1 = float(input("Please enter a number :"))
		num2 = float(input("Please enter another number :"))
		result1 = str(num1 + num2)
		print ("The result is:" + result1)
			
def user_input = "subtract":
		num3 = float(input("Please enter a number :"))
		num4 = float(input("Please enter another number :"))
		result2 = str(num3 - num4)
		print ("The result is:" + result2)
		
def user_input = "divide":
		num5 = float(input("Please enter a number :"))
		num6 = float(input("Please enter another number :"))
		result3 = str(num5 / num6)
		print ("The result is:" + result3)
	
def user_input = "multiply":
		num7 = float(input("Please enter a number :"))
		num8 = float(input("Please enter another number :"))
		result4 = str(num3 * num4)
		print ("The result is:" + result4)
	else:
		print ("Unknown input")
	elif: 
		
        print('You have not typed a valid operator, please run the program again.')