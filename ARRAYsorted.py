from numpy import *
from array import *

def main():
    a = array('i',[])
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter the value\n"))
        a.append(w)
    
    for x in range(n):
        for y in range(n):
            if a[x] < a[y] :
                t = a[x]
                a[x] = a[y]
                a[y] = t
                
    print("\n")      
    print("here is your sorted values")      
    for o in range(len(a)):
        print(a[o])
                
main()