from math import *
def main():
    print("enter the total days")
    a = int(input())
    m = a // 30
    rd = a % 30
    print("numbers of month",m,"\nthe remaining days:",rd)
main()