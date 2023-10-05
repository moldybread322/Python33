import random
score = 0
high_score = 0
attempts = 0
max_attempts = 3

while True:
    if attempts == 0:
        print ("lets do this!")
    
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    correct_answer= num1 + num2

    user_answer = int(input(f"what is {num1} + {num2}?: "))

    if user_answer == correct_answer:
        print ("correct! good stuff!")
        score += 1
    else: 
        print(f"sorry the correct answer is {correct_answer}.")
        attempts += 1
    if attempts >= max_attempts:
        print("game over, ig your just different")
        if score > high_score:
            high_score = score
            print(f"new high score is: {high_score}")

        play_again = input("play again (yes/No):")
        if play_again.lower() == "no":
            break
        else:
            score = 0
            attempts = 0