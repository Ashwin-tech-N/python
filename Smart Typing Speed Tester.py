import time
import random

sentences = [
    "Python makes programming simple and powerful.",
    "Technology is changing the world every day.",
    "Practice coding to improve your problem solving skills.",
    "Consistency is the key to becoming a good programmer."
]

sentence = random.choice(sentences)

print("\nType the following sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

# Calculate time
time_taken = end_time - start_time

# Calculate words per minute
words = len(typed_text.split())
wpm = (words / time_taken) * 60

# Calculate accuracy
correct_chars = sum(
    1 for a, b in zip(sentence, typed_text) if a == b
)

accuracy = (correct_chars / len(sentence)) * 100

print("\n--- Typing Test Results ---")
print(f"Time Taken: {time_taken:.2f} seconds")
print(f"Typing Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Characters Typed: {len(typed_text)}")
