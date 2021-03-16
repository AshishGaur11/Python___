from math import *
def main():
    print("enter the values for triangle")
    a = float(input())
    b = float(input())
    c = float(input())
    s=(a + b + c) / 2
    m = sqrt (s*(s - a)*(s - b)*(s - c))
    print(" your s is\n",s,"\nyour m is\n",m)

main()