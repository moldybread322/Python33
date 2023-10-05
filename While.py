import random

currentNumber = random.randint(1,20)
endNumber = 17


while currentNumber < endNumber:
    print ( currentNumber)
    if currentNumber > endNumber:
        print("darn")
    else:
        print ("nice")
    break