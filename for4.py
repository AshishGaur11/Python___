def main():
    print("Enter the number for factorial:")
    f = 1
    x = int(input())
    for i in range(1,x+1):
        f = f * i
    print("The factorial of",x,"is",f,".")
main()