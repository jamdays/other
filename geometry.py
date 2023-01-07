#returns the area of a circle given its radius
def CircleA (radius):
    return 3.14*radius**2 #or 3.14*pow(radius, 2)
def main():
    radStr = input ("hi user! please enter the radius of the circle so I can calculate the area")
    rad = float(radStr)
    area = CircleA(rad)
    areaStR = str(area)
    return "the area of the circle is " + areaStR
