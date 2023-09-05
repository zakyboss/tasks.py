
# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use the gross salary to find the NSSF.
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT
# ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF
basic_salary = input("Please Input your Basic salary: ")
basic_salary = int(basic_salary)
benefits = input("Please Input your Benefits: ")
benefits = int(benefits)
total = (basic_salary+benefits)
total = int(total)
nssf = (total * 0.06)
nssf = int(nssf)
if total < 18000:
    nssf_contribution = total*0.06
    print("Nssf is ", nssf_contribution)
elif total >= 18000:
    nssf_contribution = 1800*0.06
    print("Nssf is ", nssf_contribution)
else:
    pass
