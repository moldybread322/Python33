import random

score = 0
high_score = 0
attempts = 0
max_attempts = 3

difficultyLevels = ["1 digit #", "2 digit #", "3 digit #", "4 digit #", "1-5 digit #'s"]

# This functions generates random numbers based on difficuluty provided and returns the numbers
def generateRandomNumbers( difficulty ):

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
        num1 = random.randint(1000,9999)
        num2 = random.randint(1000000000,9999999999)
    elif difficulty == 5:
        num1 = random.randint(1,99999)
        num2 = random.randint(1,99999)

    return num1, num2

# This function takes in 2 numbers and returns their sum
def addNumbers( num1, num2 ):
    result = num1 + num2
    return result

# This function introduces the game
def introduceGame():
    print( "Welcome to my calculator" )
    print(f"1 for {difficultyLevels[0]}")
    print(f"2 for {difficultyLevels[1]}")
    print(f"3 for {difficultyLevels[2]}")
    print(f"4 for {difficultyLevels[3]}")
    print(f"5 for {difficultyLevels[4]}")



while True:
    introduceGame()

    userDifficultyAsAString = input( "Please select the level of difficulty (1-5): " )
    userDiffculutyAsAnInt = int( userDifficultyAsAString )

    while userDiffculutyAsAnInt < 1 or userDiffculutyAsAnInt > 5:
         userDifficultyAsAString = input( "Please make sure to select the right level of difficulty (1-5): " )
         userDiffculutyAsAnInt = int( userDifficultyAsAString )

    if attempts == 0:
        print ("lets do this!")
    
    while attempts < max_attempts:
        num1, num2 = generateRandomNumbers( userDiffculutyAsAnInt )

    # print( num1, num2 )

        correct_answer = addNumbers( num1, num2 ) 

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
            else:
                print(f"high score is still: {high_score}")

            play_again = input("play again (yes/No):")
            if play_again.lower() == "no":
                break
            else:
                score = 0
                attempts = 0