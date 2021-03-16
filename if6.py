from math import *
def main():

    print("enter values and there operation:")
    a = int(input("enter first "))
    op = input("enter operator ")
    b = int(input("enter second "))
    if op == "+" :
        print(a+b)
    elif op == "-" :
        print(a-b)
    elif op == "*" :
        print(a*b)
    elif op == "/" :
        print(a/b)
    elif op == "%":
        print(a%b)
    else:
        print("invalid operator!!")
main()