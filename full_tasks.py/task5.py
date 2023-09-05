# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them
# in three variables. Return the largest of the three. Do this without using the the
# inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take
# care of for us
number1=input("Please Insert First Number:\n")
number1=int(number1)
number2=input("Please Insert Second Number:\n")
number2=int(number2)
number3=input("Please Insert Third Number:\n")
number3=int(number3)
if number1>number2 and number1>number3:print("First Number Is Greatest")
elif number2>number1 and number2>number3:print("Second Number Is Greatest")
elif number3>number1 and number3>number2:print("Third Number Is Greatest")
else:print("ALL NUMBERS ARE EQUAL")