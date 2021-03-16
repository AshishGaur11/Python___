
def main():
    
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:")) 
    
    matrix1 = [] 
    print("Enter the entries rowwise:") 
    
    
    for i in range(R):          #for loop for row entries 
        a =[] 
        for j in range(C):      #for loop for column entries 
            a.append(int(input())) 
        matrix1.append(a) 
    
    matrix2 = [] 
    print("Enter the entries rowwise:") 
    
    
    for i in range(R):          #for loop for row entries 
        b =[] 
        for j in range(C):      #for loop for column entries 
            b.append(int(input())) 
        matrix2.append(b) 








    print("matrix 1 \n")
# For printing the matrix 
    for i in range(R): 
        for j in range(C): 
            print(matrix1[i][j], end = " ")
        print() 

    print("matrix 2 \n") 
# For printing the matrix 
    for i in range(R): 
        for j in range(C): 
            print(matrix2[i][j], end = " ")
        print()   

    print("matrix added \n")     
        
    for i in range(R): 
        for j in range(C): 
            print(matrix1[i][j]+matrix2[i][j], end = " ")
        print()  
        
main()
    
    
   