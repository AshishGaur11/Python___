def main():
    w = int(input("Enter to make triangle\n"))
    i = 1
    while i <= w :
        j = 1
        while j <= i :
            print(j,end = "")
            j += 1
        print("\n")
        i += 1

main()