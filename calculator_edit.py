import sys


def add(num1, num2):
    result1 = str(num1 + num2)
    print(f"The result is: {result1}")


def subtract(num3, num4):
    result2 = str(num3 - num4)
    print(f"The result is: {result2}")


def divide(num5, num6):
    result3 = str(num5 / num6)
    print(f"The result is: {result3}")


def multiply(num7, num8):
    result4 = str(num7 * num8)
    print(f"The result is: {result4}")


while True:
    print("1. If you want to add two numbers")
    print("2. If you want to subtract two numbers")
    print("3. If you want to divide two numbers")
    print("4 .If you want to multiply two numbers")
    print("5. If you want to end the program, please type 'quit'")
    choice = input("Enter choice (1, 2, 3, 4): ")

    if choice == "1":
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        add(num1, num2)

    elif choice == "2":
        num3 = float(input("Please enter a number: "))
        num4 = float(input("Please enter another number: "))
        subtract(num3, num4)

    elif choice == "3":
        num5 = float(input("Please enter a number: "))
        num6 = float(input("Please enter another number: "))
        divide(num5, num6)

    elif choice == "4":
        num7 = float(input("Please enter a number: "))
        num8 = float(input("Please enter another number: "))
        multiply(num7, num8)

    elif choice == "quit":
        sys.exit("Quit")
