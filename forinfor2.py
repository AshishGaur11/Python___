def fif():


    x = int(input("Enter the value for prime number: \n"))
    a = 1
    while a <= x :
        f = 0
        i = 1
        while i <= a :
            if a % i == 0 :
                f = f + 1
            i += 1
        if f == 2 :
            print(a)
        a += 1

fif()