#Factor finding
'''
num = int(input("Enter number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
'''

#count the factor
'''
num = int(input("Enter number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of factors: ", count)
'''

#Perfect Number

num = int(input("Enter number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i
if total == num:
    print("Prefect number")
else:
    print("Not a perfect number")
