# loops in python
'''
for i in range(5):
    print("HELLO")
'''
# for range
'''
for i in range(5):
    print(i)
'''

'''
for i in range(1, 6):
    print(i)
'''

'''
for i in range(1, 11, 3): #(start, stop, step)
    print(i)
'''

'''
for i in range(10, 0, -1):
    print(i)
'''

#loop + condition
#print even number
'''
n = int(input("Enter the starting number:"))
m = int(input("Enter the ending number:"))

for num in range(n, m):
    if num % 2 == 0:
        print(num)
'''

#print odd number
'''
n = int(input("Enter the starting number: "))
m = int(input("Enter the ending number: "))

for odd in range(n, m):
    if odd % 2 != 0:
        print(odd)
'''

# sum of number

n = int(input("Enter the starting number: "))
m = int(input("Enter the ending number: "))
total = 0

for number in range(n, m):
    total = total + number
print(total)
