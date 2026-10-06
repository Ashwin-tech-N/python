#prime number
'''
num = int(input("Enter number: "))

if num < 2:
    Print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
'''
#Prime 1 to 100
'''
h = int(input("Enter the range: "))

for num in range(2, h):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
'''

#Armstrong Number

num = int(input("Enter number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10

if  original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
