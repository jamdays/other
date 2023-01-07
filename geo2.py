from geometry import *

def rectangleA(l,w):
    area = l*w
    return area
def main2():
    l = input ("what is the length of your rectangle? \n ")
    w = input ("what is the width of your rectangle? \n ")
    l = float(l)
    w = float(w)
    area = rectangleA(l,w)
    areaStr = str(area)
    return "the area of your rectagle is " + areaStr
