def main():
    print("enter three number to find the greatest")
    a = int(input())
    b = int(input())
    c = int(input())
    if a>b and a>c :
        print(a," is greater than b,c")
    elif b>c :
        print(b," is greater than c,a")
    else:
        print(c,"is greater than a,b ")
main()