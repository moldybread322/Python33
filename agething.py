import random

age = random.randint (18,40)
wadge = random.randint (18,40)



while True:
    print(age,wadge)
    if age < wadge:
        print("Next year it will be more")
        wadge += 1
        age += 1
    else:
        print ("you'll be fine with this amount")
        
    No_im_not = input("im not fine with this amount, add 1 (yes/No):")
    if No_im_not.lower() == "no":
        wadge += 1
    
    if age > 99:
        print("you have died")