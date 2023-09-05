# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list
# below if we know that the stock is the last digit in every array/list.
products = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'],
            ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
total_stock = 0
for prod in products:
    stock = int(prod[2])
    total_stock += stock
print("The total stock in the company is:", total_stock)
