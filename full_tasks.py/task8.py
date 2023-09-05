# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than
# 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it
# should give the driver one demerit point and print the total number of demerit
# points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more
# than 12 points, the function should print: “License suspended”.
speed = input("Please Insert Speed:\n")
speed = int(speed)
if speed == 70:
    print("Okay")
elif ((speed-70)/5) == 1:
    print("1 point")
elif ((speed-70)/5) == 2:
    print("2 points")
elif ((speed-70)/5) == 3:
    print("3 points")
elif ((speed-70)/5) == 4:
    print("4 points")
elif ((speed-70)/5) == 5:
    print("5 points")
elif ((speed-70)/5) == 6:
    print("6 points")
elif ((speed-70)/5) == 7:
    print("7 points")
elif ((speed-70)/5) == 8:
    print("8 points")
elif ((speed-70)/5) == 9:
    print("9 points")
elif ((speed-70)/5) == 10:
    print("10 points")
elif ((speed-70)/5) == 11:
    print("11 points")
elif ((speed-70)/5) >= 12:
    print("License Revoked")
else:
    print("Okay")
