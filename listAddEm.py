

def addEmUp(listOfNums):
    total = 0
    for val in listOfNums:
        total += val
    return total


def totalNumsForUser():
    NumberList = []
    print("hi you can enter any number and I will add them")
    LengthList = int(input("how many numbers are you gonna ask me to add together?\n"))
    count = 0
    while count < LengthList:
        inputVal = int(input("enter number\n"))
        NumberList.append(inputVal)
        count += 1
    print("okay you gave me " + str(NumberList))
    total = addEmUp(NumberList)
    print("your total is " + str(total))

    
def loopWhileRaining():
    print("hi, look outside!")
    response = input("is it raining? (y/n)\n")
    raining = ( response == "y")
    while raining:
        print("go dance in the rain!!!")
        raining = (input("is it still raining?(y/n) \n") == "y")
    print("yay!!!!!!!!!!!!!!!!!!!!!!!!")


def main():
    totalNumsForUser()
    print()
    loopWhileRaining()
    print("session is over type main() to start again!")

main()
