# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable
# income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
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
# PAYEE
if taxable_income >= 0 and taxable_income <= 24000:
    print("Payee Is", taxable_income*0.01)
elif taxable_income >= 24000 and taxable_income <= 32333:
    print("Payee is", taxable_income*0.25)
elif taxable_income > 32333:
    print("Payee Is ", taxable_income*0.30)
else:
    pass
