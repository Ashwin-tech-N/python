#factorial
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i
print("factorial is:", fact)
'''

#count the number of digits
'''
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count = count + 1
print("Number of digits: ", count)
'''

#reverse a Number
'''
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number is: ",reverse)
'''
#palindrome

num = int(input("Enter the number: "))
reverse = 0
rev = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if rev == reverse:
    print("it is an palindrome")
else:
    print("not a palindrome")
