def sum():
    print("Enter the number for sum them")
    m = int(input())

    i = 0
    while m != 0 :
        x = m % 10
        print(x)
        i = i + x
        m = m // 10

    print("\n")
    print(i)
sum()