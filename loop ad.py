# the flag pattern
'''
k = int(input("Enter the number:"))
f = int(input("Enter the number you want to found:"))

found = False

for i in range(k):
    if i == f:
        found = True
        break
    print(i)
if found:
    print("The number is Found: ", f)
else:
    print("Not found")
'''
# prime checker
'''
num = int(input("Enter  the number: "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not a prime")
'''
#prime print 1 to 100

for num in range(2, 101):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
