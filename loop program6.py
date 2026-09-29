'''
age = int(input("enter your age:"))

if age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


num = int(input("enter any number:"))

if num > 0:
    print("positive")
else:
    print("negative")
    

num = int(input("Enter any number:"))

if num % 2 == 0:
    print("even")
else:
    print("odd")

mark = int(input("Enter your mark:"))

if mark >= 95:
    print("you get S grade")
elif mark >= 85:
    print("you get A grade")
elif mark >= 75:
    print("you get B grade try to get more")
elif mark >= 70:
    print("you get c grade need improvement")
elif mark >= 60:
    print("you get D grade just pass dont feel good ok")
else:
    print("fail, good wasting you fathers money")
    

age = int(input("Enter your age:"))
salary = int(input("Enter your salary:"))

if age >= 18 and salary >= 20000:
    print("you are eligible for this")
else:
    print("you are not eligible for this")


date = int(input("enter your date:"))

if date == 20 or date == 18:
    print("good date")
else:
    print("your are not a men")



log = False

if not log:
    print("rich")



age = int(input("enter your age:"))
citizen = input("If your a india citizen:")

if age >= 18:
    if citizen == "yes" or "y":
        print("your are eligiblle for vote")
    else:
        print("not a citizen")
else:
    print("under age")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("both are equal")



a = 10
b = 25
c = 15

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

import calendar

year = 2025
print(calendar.isleap(year))


'''

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
