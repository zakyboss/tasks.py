# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them
# to find the gross salary then uses the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:
basic_salary = input("Please Input your Basic salary:\n")
basic_salary = int(basic_salary)
benefits = input("Please Input your Benefits:\n")
benefits = int(benefits)
gross_salary= (basic_salary+benefits)
print(gross_salary)
if gross_salary <= 6000:
    print(150)
elif gross_salary <= 7999:
    print(300)
elif gross_salary <= 11999:
    print(400)
elif gross_salary <= 14999:
    print(500)
elif gross_salary <= 19999:
    print(600)
elif gross_salary <= 24999:
    print(750)
elif gross_salary <= 29999:
    print(850)
elif gross_salary <= 34999:
    print(900)
elif gross_salary <= 39999:
    print(950)
elif gross_salary <= 44999:
    print(1000)
elif gross_salary <= 49999:
    print(1100)
elif gross_salary <= 59999:
    print(1200)
elif gross_salary <= 69999:
    print(1300)
elif gross_salary <= 79999:
    print(1400)
elif gross_salary <= 89999:
    print(1500)
elif gross_salary <= 99999:
    print(1600)
elif gross_salary > 100000:
    print(1700)
