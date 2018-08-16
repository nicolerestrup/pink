operation = input("Please type the operation you would like to complete: \n + for addition \n - for subtraction \n * for multiplication \n / for divation \n")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your 2nd number: "))
#Addition
if operation == "+":
    print("{} + {} = ".format(number1, number2))
    print(number1 + number2)
#Subtraction
elif operation == "-":
    print("{} - {} = ".format(number1, number2))
    print(number1 - number2)
#Multiplication
elif operation == "*":
    print("{} * {} = ".format(number1, number2))
    print(number1 * number2)
#Divation
elif operation == "/":
    print("{} / {} = ".format(number1, number2))
    print(number1 / number2)
else:
    print("You haven't chosen a correct operation. Run the program again!")
