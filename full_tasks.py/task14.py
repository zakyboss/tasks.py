# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should
# only accept numbers and floats only or otherwise display an error “invalid character
# entered” and take the user to re-enter the inputs .
def add_two_values():
    try:
        value1 = float(input("Enter the first number: "))
        value2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid character entered. Please enter numbers or floats only.")
        return add_two_values()
    else:
        return value1 + value2


print(add_two_values())
