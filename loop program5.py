#palindrom program
'''
n = int(input("Enter the number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("its an palindrom")
else:
    print("not a palindrom")
'''

#nested loop
'''
for i in range(3):
    for j in range(3):
        print(i, j)
'''

#nested loop pattern
'''
for i in range(5):
    print("*")
'''

for i in range(3):
    for j in range(4):
        print("*", end = ' ')
    print()
