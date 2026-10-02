#accumulator
'''
k = int(input("Enter the number: "))

total = 0

for i in range(1, k):
    total = total + i
print(total)


p = int(input("Enter the number: "))
count = 0
for i in range(1, p):
    if i % 2 == 0:
        count = count + 1
print(count)
'''

#largest number
'''
largest = list(map(int, input("Enter the list: ").split()))
l = int(input("Enter the number: "))
for num in(largest):
    if num > l:
        l = num
print(l)
'''

#prime number

num = int(input("Enter number: "))

is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime")
