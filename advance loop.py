# Triangle Pattern
'''
l = int(input("Enter the range: "))

for i in range(1, l):
    for j in range(i):
        print("*", end = " ")
    print()
'''
#number pattern
'''
k = int(input("Enter the number range: "))

for i in range(1, k):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
'''

#another number patterns
'''
y = int(input("Enter the range number: "))

for i in range(1, y):
    for j in range(i):
        print(i, end = " ")
    print()
'''
#multiplication table
'''
k = int(input("Enter the last before table number you need: "))

for i in range(1, k):
    for j in range(1, 11):
        print(i * j, end = " ")
    print()
'''
#break in nested loop
'''
for i in range(5):
    for j in range(5):
        if j == 5:
            break
        print(i, j)
'''
#continue in Nested loop
'''
for i in range(3):
    for j in range(5):

        if j == 1:
            continue
        print(j, end = " ")
    print()
'''
#while + break
'''
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
    print("you entered:", num)
'''

#Simple menu

while True:
    print("1. Add")
    print("2. subtract")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", a + b)
    elif choice == 2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Result: ", a - b)
    elif choice == 3:
        print("Program end!")
        break
    else:
        print("Enter the correct number only....")
