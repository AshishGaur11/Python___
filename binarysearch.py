from array import *

def main():

    a = []
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter next values\n"))
        a.append(w)
        
        
    item = int(input("Enter the value for search\n"))
    l = 0
    h = 9
    md = 1
    
    while l <= h:
        md = (l+h)//2
        if item == a[md] :
            print("value is found",md + 1)
            break
        elif item < a[md] :
            h = md - 1
        else :
            l = md + 1
                 
main()

