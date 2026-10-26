
import random

# Demo user account
users = {
    "ashwin": {
        "password": "Python@123",
        "verified": True
    }
}

def verify_user():
    username = input("Enter username: ").strip().lower()

    if username not in users:
        print("User not found!")
        return

    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")

        if password == users[username]["password"]:
            print("Password verified!")
            break

        attempts -= 1
        print("Incorrect password.")
        print("Attempts remaining:", attempts)

    if attempts == 0:
        print("Verification failed. Access denied.")
        return

    otp = str(random.randint(100000, 999999))
    print("Demo OTP (for practice only):", otp)

    entered_otp = input("Enter OTP: ")

    if entered_otp == otp:
        print("OTP verified successfully!")
        print("Welcome,", username)
        print("Verification complete.")
    else:
        print("Invalid OTP. Access denied.")

print("===== USER VERIFICATION BOT =====")
verify_user()
