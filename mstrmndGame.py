import random

def makeGuess(target):
    colors = ["r", "g", "o", "y", "p", "v", "i", "t"]
    guess = []
    for let in target: 
        playerGuess = input("guess one of the following letters" + str(colors) + "\n")
        guess.append(playerGuess)
    return guess

def checkGuess(guess, target):
    target1 = target.copy()
    result = ''
    for letter in target:
        if letter == guess[target.index(letter)]:
            result += "b"
            target1.remove(letter)
    for guessLet in guess:
        for letter in target1:
            if guessLet == letter:
                result +="w"
                target1.remove(letter)
    for letter in target1:
        result += "-"
    return result 
        
    

                            
def mstrmind():
    colors = ["r", "g", "o", "y", "p", "v", "i", "t"]
    target = random.sample(colors, 4)
    correctGuess = False
    count = 0
    while count < 11 or correctGuess == True:
        okGuess = False 
        while okGuess == False: 
            guess = makeGuess(target)
            again = input ('is this the Guess you want to make??' + str(guess) + '\n (y/n)')
            if again == 'y':
                okGuess = True
        result = checkGuess(guess, target)
        if result == "bbbb":
            correctGuess = True
            return ('you won by guessing ' + str(target) + ' in only ' + str(count) + " tries WOOO!")
        else:
            print(result)
            print("try again")
            count += 1
    return ("game over the answer was" + str(target))
            
            

    
    
