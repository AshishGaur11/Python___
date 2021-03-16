from math import *

def main():

    print("enter the value for simple interest")
    p = float(input("principle"))
    r = float(input("Rate"))
    t = float(input("Time"))
    si =  (p * t * r)  / 100
    print( "SI is ", + si )

main()
