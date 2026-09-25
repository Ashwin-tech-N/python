#multiplication Table
'''
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
'''

#while loop
'''
n = int(input("Enter a number: "))
count = 1

while count <= n:
    print(count)
    count = count + 1
'''
#break
'''
for i in range(1, 11):
    if i == 5:
        break
    print(i)
'''

#continue
'''
for i in range(1, 6):

    if i == 3:
        continue
    print(i)
'''

#exercises
#print 20 to 1
'''
for i in range(1, 21):
    print(i)
'''
'''
count = 1

while count <= 20:
    print(count)
    count = count + 1
'''
#print 20 down to 1
'''
for i in range(20, 0, -1):
    print(i)
'''

#print even numbers between 1 to 50
'''
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
'''

#print odd numbers between 1 to 50

for i in range(1, 50):
    if i % 2 != 0:
        print(i)
