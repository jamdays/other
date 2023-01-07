import random

def guessNumber1():
    print("I will pick a number 1-10, and you have to guess it")
    target = random.randint(1,10)
    guess = int(input("OK, enter your guess: "))
    if target == guess:
        print("you got it! this is your lucky day!")
    else:
        print("Sorry! Better luck next time")

def guessNumber2():
    print("I will pick a number 1-10, and you have to guess it")
    target = random.randint(1,10)
    guess = int(input("OK, enter your guess: "))
    while target != guess:
        guess = int(input("Nice try, guess again:"))
    print("Nice, you got it!!")

def guessNumber3():
    print("I will pick a number 1-10, and you have to guess it")
    target = random.randint(1,10)
    guess = int(input("OK, enter your guess: "))
    count = 1 
    while target != guess:
        guess = int(input("Nice try, guess again:"))
        count += 1
    print("Nice, you got it!! in only " + str(count) + " tries")

def guessNumber4():
    print("I will pick a number 1-10, and you have 3 tries to guess it")
    target = random.randint(1,10)
    guess = int(input("OK, enter your guess: "))
    count = 1 
    while target != guess and count < 3:
        guess = int(input("Nice try, guess again:"))
        count += 1
    if target == guess:
        print("Nice, you got it!! in only " + str(count) + " tries")
    else:
        print("you lose, maybe try again?")

def guessNumber5():
    print("I will pick a number 1-100, and you have 6 tries to guess it")
    target = random.randint(1,100)
    guess = int(input("OK, enter your guess: "))
    count = 1 
    while target != guess and count < 6:
        if guess > target:
            print("too high")
        else:
            print("too low")
        guess = int(input("Guess again!:"))
        count += 1
    if target == guess:
        print("Nice, you got it!! in only " + str(count) + " tries")
    else:
        print("you lose, the number was " + str(target) + " maybe try again?")
    
