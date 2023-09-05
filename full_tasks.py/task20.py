# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf + nssf + payee)
basic_salary = input("Please Input your Basic salary: ")
basic_salary = int(basic_salary)
benefits = input("Please Input your Benefits: ")
benefits = int(benefits)
gross_salary = (basic_salary+benefits)
print("This Is gross Salary", gross_salary)
if gross_salary <= 6000:
    nhif = 150
elif gross_salary <= 7999:
    nhif = 300
elif gross_salary <= 11999:
    nhif = 400
elif gross_salary <= 14999:
    nhif = 500
elif gross_salary <= 19999:
    nhif = 600
elif gross_salary <= 24999:
    nhif = 750
elif gross_salary <= 29999:
    nhif = 850
elif gross_salary <= 34999:
    nhif = 900
elif gross_salary <= 39999:
    nhif = 950
elif gross_salary <= 44999:
    nhif = 1000
elif gross_salary <= 49999:
    nhif = 1100
elif gross_salary <= 59999:
    nhif = 1200
elif gross_salary <= 69999:
    nhif = 1300
elif gross_salary <= 79999:
    nhif = 1400
elif gross_salary <= 89999:
    nhif = 1500
elif gross_salary <= 99999:
    nhif = 1600
elif gross_salary > 100000:
    nhif = 1700
print("This Is Nhif", nhif)
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
# PAYEe

if taxable_income >= 0 and taxable_income <= 24000:
    payee = ("Payee Is", taxable_income*0.01)
elif taxable_income >= 24000 and taxable_income <= 32333:
    payee = ("Payee is", taxable_income*0.25)
elif taxable_income > 32333:
    payee = ("Payee Is ", taxable_income*0.30)
else:
    pass
print("This Is Payee", payee)

# net_salary= gross_salary-(nhif +nhdf+nssf +payee)
net_salary = gross_salary-((Nhdf)+(nhif)+(nssf))
print('thiss is net salary', net_salary)
