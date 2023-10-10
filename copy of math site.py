import random
score = 0
high_score = 0
attempts = 0
max_attempts = 3

difficultyLevels = ["easy", "normal", "hard", "impossible"]

# This functions generates random numbers based on difficuluty provided and returns the numbers
def generateRandomNumbers( difficulty ):
    if difficulty == 1:
        num1 = random.randint(1,9)
        num2 = random.randinft(1,9)
    elif difficulty == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    elif difficulty == 3:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)
    elif difficulty == 4:
        num1 = random.randint(1000000000,9999999999)
        num2 = random.randint(1000000000,9999999999)

    return num1, num2

# This function takes in 2 numbers and returns their sum
def addNumbers( num1, num2 ):
    result = num1 + num2
    return result

# This function introduces the game
def introduceGame():
    print( "Welcome to my calculator" )
    print(difficultyLevels)

while True:
    introduceGame()

    userDifficultyAsAString = input( "Please select number of digits: " )
    userDiffculutyAsAnInt = int( userDifficultyAsAString )

    if attempts == 0:
        print ("lets do this!")
    
    num1, num2 = generateRandomNumbers( userDiffculutyAsAnInt )
    
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

        play_again = input("play again (yes/No):")
        if play_again.lower() == "no":
            break
        else:
            score = 0
            attempts = 0