import random

score = 0
high_score = 0
attempts = 0
max_attempts = 3
difficultyLevels = ["easy", "normal", "hard", "impossible", "random digits"]

def generateRandomNumbers(difficulty):
    if difficulty == 1:
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
    elif difficulty == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    elif difficulty == 3:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)
    elif difficulty == 4:
        num1 = random.randint(1000000000,9999999999)
        num2 = random.randint(1000000000,9999999999)
    elif difficulty == 5:
        num1 = random.randint(1,99999)
        num2 = random.randint(1,99999)

    return num1, num2

def addNumbers(num1, num2):
    result = num1 + num2
    return result

def introduceGame():
    print( "Welcome to my calculator" )
    print(f"1 for {difficultyLevels[0]}")
    print(f"2 for {difficultyLevels[1]}")
    print(f"3 for {difficultyLevels[2]}")
    print(f"4 for {difficultyLevels[3]}")
    print(f"5 for {difficultyLevels[4]}")

while True:
    introduceGame()

    userDifficultyAsAString = input("Please select the level of difficulty (1-5): ")
    userDifficultyAsAnInt = int(userDifficultyAsAString)

    while userDifficultyAsAnInt < 1 or userDifficultyAsAnInt > 5:
        userDifficultyAsAString = input("Please make sure to select the right level of difficulty (1-5): ")
        userDifficultyAsAnInt = int(userDifficultyAsAString)

    if attempts == 0:
        print("Let's do this!")

    while attempts < max_attempts:
        num1, num2 = generateRandomNumbers(userDifficultyAsAnInt)

        correct_answer = addNumbers(num1, num2)

        user_answer = int(input(f"What is {num1} + {num2}?: "))

        if user_answer == correct_answer:
            print("Correct! Good stuff!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
            attempts += 1

        if attempts >= max_attempts:
            print("Game over! You're just different.")
            if score > high_score:
                high_score = score
                print(f"New high score is: {high_score}")
            else:
                print(f"High score is still: {high_score}")

            play_again = input("Play again (yes/No): ")
            if play_again.lower() == "no":
                break
            else:
                score = 0
                attempts = 0
