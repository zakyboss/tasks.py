# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0
# and 100.Then output the correct grade:
# A > 79 , B - 60 to 79, C - 59 to 49, D - 40 to 49, E - less 40
marks = input("Please Insert Your Marks: ")
marks = int(marks)
if marks >= 79:
    print("A")
elif marks <= 79 & marks >= 61:
    print("B")
elif marks <= 59 & marks >= 49:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("E")
