#input validation
'''
age = int(input("enter age:"))
if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Adult")
else:
    print("Minor")
'''

#range check
'''
num = int(input("enter the number:"))

if 10 <= num <=50:
    print("Valid")
else:
    print("invalid")
'''

#real time example
'''
username = input("Username: ")
password = input("Password: ")

if username == "ashwin":
    if password == "1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("user not found!")
'''

#ternary operator
'''
age = int(input("Enter your age:"))

result = "Adult" if age >= 18 else "Minor"
print(result)
'''

#boolean variable
'''
is_login = False

if is_login: # not is_login -> for False
    print("Welcome")
else:
    print("please login")
'''

#Input: 10 20 30
#Output: All positive
'''
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > 0 and b > 0 and c > 0:
    print("All positive")
elif a < 0 and b < 0 and c < 0:
    print("All negative")
else:
    print("Mixed")
'''

#challenge1

bill = int(input("Enter the unit used: "))

if 0 < bill <= 100:
    print("Amount you want to pay: ",bill * 2)
elif bill == 0:
    print("No unit consume")
elif bill < 0:
    print("Invalid units")
elif bill <= 200:
    print("Amount you want to pay: ",bill * 3)
elif bill <= 300:
    print("Amount you want to pay: ",bill * 5)
else:
    print("Amount you want to pay: ",bill * 7)


        
    
