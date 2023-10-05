import random

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    # Generate random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Ask the user to input their answer
    user_answer = int(input(f"What is {num1} + {num2}? "))

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Correct! Good job!")
        break  # Exit the loop if the answer is correct
    else:
        print(f"Sorry, the correct answer is {correct_answer}. Try again.")
        attempts += 1

if attempts == max_attempts:
    print(f"You've reached the maximum number of attempts ({max_attempts}). Game over.")
else:
    print("Great job! You got the answer right!")
