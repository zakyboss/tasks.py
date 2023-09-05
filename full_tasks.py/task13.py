# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if
# they are equal to “admin@mail.com” and password is “Admin@123” , if so then print
# “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3
# tries after which it notifies you that you have been blocked.

attempts = 0

while attempts < 3:
    username = input("Enter your username")
    password = input('Enter your password: ')

    if username == "" and password == 'admin@123':
        print('You have successfully logged in.')
        break
    elif attempts >= 2:
        print("You have been blocked,Call Agent")
    else:
        print('Invalid Email,please try again.')
    attempts += 1
    continue
