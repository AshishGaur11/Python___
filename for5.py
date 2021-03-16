def main():
    print("Enter the value:")
    x = int(input())
    print("Enter the power of the value:")
    y = int(input())
    z = 1
    for i in range(1,y+1):
        z = z * x
    print(z,"is your ans")

main()