from random import *

def rochambo():
    answer = input ("lets play some rochambo! choose rock(r) paper(p) or scissors(s)\n")
    myPick = randint(1,3)
    if answer == "r":
        answer = 1
    elif answer == "p":
        answer = 2
    else:
        answer = 3
    if myPick == answer:
        print ("draw")
    elif myPick == 1 + answer or myPick == answer - 2:
        print ("loss")
    else:
        print("win")
    return (answer, myPick)

        
        
