def reverse():
    x = int()

    s = int(input("Enter the value for reverse the number:\n"))
    while s != 0 :

        x = s % 10
        print( x , end = "" )

        s = s // 10






reverse()