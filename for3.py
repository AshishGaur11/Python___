def main():

    print("Enter the range of number:")
    h = int(input())
    print("which number's divisibility:")
    e = int(input())
    c = int()
    c = 0
    for s in range(1,h+1) :
        if s%e==0 :
            c = c + 1

    print(c, "numbers are divisible in the range of ",h ,"by",e,".")
main()
