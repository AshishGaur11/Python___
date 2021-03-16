from numpy import *
from array import *

def main():
    a = array('i',[])
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter next values\n"))
        a.append(w)
    b = array('i',[])
    x = int(input("Enter the length of array\n"))
    for y in range(x):
        w = int(input("Enter next values\n"))
        b.append(w)
    
    
    c = array('i',[])  
    m = n
    if m == x :
        for q in range(m):
            c.append(a[q] + b[q])
        
    
        print("here are your values\n")
        for o in range(len(c)):
            print(c[o]) 
        main()
    else:
        print("not possible!!")
        
        main()

main()