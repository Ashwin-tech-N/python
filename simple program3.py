# multiple cnditions with and
'''
age = int(input("enter your age:"))
marks = int(input("enter your mark:"))

if age >= 18 and marks >= 60:
    print("eligible")
else:
    print("you are not eligible for this")
'''

#fees are paid
'''
attendance = int(input("enter your attendance percentage:"))
fees_paid = input("if you pay your college fees:")
if fees_paid == "y" or "yes":
    fees_paid = True
    if attendance >= 80 and fees_paid:
        print("Allowed")
    else:
        print("not allowed")
'''

#mulitiple condition with or
'''
day = input("Enter the day:")

if day == "saturday" or "sunday":
    print("Holiday")
else:
    print("Working day")  
'''

#combining and + or
'''
mark = int(input("Enter your mark:"))
attendance = int(input("enter your attendance percentage:"))

if mark >= 90 or (mark >= 70 and attendance >= 90):
    print("Eligible")
else:
    print("Not eligible")
'''
#nested if

age = int(input("enter your age:"))
citizen = input("If you are an Indian:")

if age >= 18:
    if citizen == "yes" or "y":
        print("Elligible")
    else:
        print("Not a citizen")
else:
    print("Under 18")
