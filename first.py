def f(x):
    return x + 4
def sayHi():
    name = input ("whats your name?")
    ageStr = input ("jow old are you")
    age = int(ageStr)
    newAge = age +5
    newAgeStr = str(newAge)
    return (name + " is now coding python and in 5 years" + name + " will be " + newAgeStr)  
def checkWeather():
    result = input ("is it raining?(y/n)")
    isRaining = (result == 'y')
    if isRaining:
        print("WEAR BOOTS")
        print("WEAR JACKET")
    else:
        print ("GO OUTSIDE!!!!!!!!!!")
    print ("GOOD DAY MATE")
    
