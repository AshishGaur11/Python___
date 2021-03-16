from array import *
def fun():

    """NEW TAKING INPUT FROM USER"""
    c = array('i',[]) # this is also dynamic
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter next values\n"))
        c.append(w)
    print("here are your values\n")
    for o in range(len(c)):
        print(c[o])

    """search algo"""
    i = int(input("Enter the value for search\n"))

    k=1
    for m in c:
        if m == i:
            print("ON position number",k)
            break
        k += 1

    fun()

fun()