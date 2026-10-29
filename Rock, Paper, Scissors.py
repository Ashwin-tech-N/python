
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Choose (1/2/3/4): ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    user = choices[int(choice) - 1]
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

print("\n===== FINAL SCORE =====")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Thanks for playing!")
