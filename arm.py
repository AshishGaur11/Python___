from math import *
def arm():
    m = int(input("Enter to get armstrong value\n"))
    t = int(input("Enter numbers of number \n"))
    i = 0
    d = m
    while m!=0 :
        x = m % 10
        i = i + pow(x,t)
        m = m // 10
    if d == i :
        print("yes its a armstrong\n")
    else:
        print("not armstrong\n")


arm()