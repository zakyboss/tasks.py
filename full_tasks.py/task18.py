# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF)
basic_salary = input("Please Input your Basic salary: ")
basic_salary = int(basic_salary)
benefits = input("Please Input your Benefits: ")
benefits = int(benefits)
gross_salary = (basic_salary+benefits)
nssf = (gross_salary * 0.06)
nssf = int(nssf)
if gross_salary < 18000:
    nssf_contribution = gross_salary*0.06
    print("Nssf is ", nssf_contribution)
elif gross_salary >= 18000:
    nssf_contribution = 1800*0.06
    print("Nssf is ", nssf_contribution)
else:
    pass
Nhdf = gross_salary*0.015
taxable_income = gross_salary-(nssf+Nhdf)

print("taxable income is", taxable_income)
