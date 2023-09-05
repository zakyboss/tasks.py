# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that
# the user would not enter any two numbers which are the same.

number1 = input("Please Insert First Number:\n")
number1 = int(number1)
number2 = input("Please Insert Second Number:\n")
number2 = int(number2)
number3 = input("Please Insert Third Number:\n")
number3 = int(number3)
number4 = input("Please Insert Third Number:\n")
number4 = int(number4)
if number1 > number2 and number1 > number3 and number1 > number4:
    print("First Number Is Greatest")
elif number2 > number1 and number2 > number3 and number2 > number4:
    print("Second Number Is Greatest")
elif number3 > number1 and number3 > number2 and number3 > number4:
    print("Third Number Is Greatest")
elif number4 > number1 and number4 > number2 and number4 > number3:
    print("The Forth Number Is greatest")
else:
    print("Please dont insert two equal numbers")
