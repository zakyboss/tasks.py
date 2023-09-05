# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program input a password. Give them only 4 attempts to check the
# passwords entered against “admin@123”. If the password is correct access is
# granted. After you show them a message , the account is blocked.

attempts = 0

while attempts < 3:
    password = input('Enter your password: ')

    if password == 'admin@123':
        print('You have successfully logged in.')
        break
    elif attempts >= 2:
        print("You have been blocked,Call Agent")
    else:
        print('Invalid Email,please try again.')
    attempts += 1
    continue
