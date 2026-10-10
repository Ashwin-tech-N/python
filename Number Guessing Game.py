
import random

secret = random.randint(1, 100)
attempts = 7

print("Guess the number between 1 and 100!")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You won!")
        break
    elif guess < secret:
        print("Too low! Try a bigger number.")
    else:
        print("Too high! Try a smaller number.")

    attempts -= 1
    print("Attempts remaining:", attempts)

if attempts == 0:
    print("Game over! The number was", secret)
