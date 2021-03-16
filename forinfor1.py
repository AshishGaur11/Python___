def main():
    f = int(input("Enter the up to where you table\n"))
    for i in range(2,f+1):
        for j in range(1,11):
            o = i * j
            print("\t",o,end ="")
        print("\n")


def ok():
    f = int(input("Enter the up to where you table\n"))
    for i in range(1,11):
        for j in range(2,f+1):
            o = i * j
            print("\t",o,end ="")
        print("\n")
main()
ok()
