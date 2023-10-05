import random
max_attempts = 3
attempts = 0
score = 0
high_score = 0

while attempts < max_attempts:
    num2 = random.randint(1,10)
    num1 = random.randint(1,10)


    correct_answer = num1 + num2

    user_answer = int(input(f"what is {num1} + {num2}?: "))

    if user_answer == correct_answer:
        print("correct!")
        break
    else:
        print(f"incorrect, {correct_answer} is correct")
        attempts += 1
        # Another way to increment
        # attempts = attempts + 1

    if attempts == max_attempts:
        print("you have reached the maximum chances of answering the questions")
    else:
        print("try again")