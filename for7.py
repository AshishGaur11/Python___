def main():
    print("Enter the Value:")
    f = 0
    c = int(input())
    for i in range(1,c+1):
        if c % i == 0 :
            f = f + 1
    if f == 2 :
        print("This is a PRIME a number!!")
    else:
        print("This is a NOT A PRIME number!!")
main()