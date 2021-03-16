def main():
    print("enter marks")
    a = int(input())
    if a>=80:
        print("a grade")
    elif a<=79 and a>=60:
        print("b grade")
    elif a<=59 and a>=40:
        print("c grade")
    elif a<=39 and a>=30:
        print("d grade")
    else:
        print("fail")
main()
