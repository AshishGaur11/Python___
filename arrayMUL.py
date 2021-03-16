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
            
    g = array('i',[])  
    m = n
    if m == x :
        for q in range(m):
            g.append(a[q] * b[q])
        
    
        print("here are your values of ADD \n")
        for o in range(len(c)):
            print(c[o]) 
        
        
        print("here are your values of MUL\n")
        for o in range(len(g)):
            print(g[o]) 
        main()
    
    else:
        print("not possible!!")
        
        main()

main()




R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 