def matmul():
    
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:")) 
    
    matrix1 = [] 
    print("Enter the entries rowwise:") 
    
    
    for i in range(R):          
        a =[] 
        for j in range(C):      
            a.append(int(input())) 
        matrix1.append(a) 
    
    matrix2 = [] 
    print("Enter the entries rowwise:") 
    
    
    for i in range(R):          
        b =[] 
        for j in range(C):      
            b.append(int(input())) 
        matrix2.append(b) 


    ca = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]


    for i in range(R):
        for j in range(C):
            for k in range(C):
                ca[i][j] = ca[i][j] + matrix1[i][k] * matrix2[k][j]
 
 
    
    
    
    print("your multiplied matrix \n")
    for i in range(R): 
        for j in range(C): 
            print(ca[i][j], end = " ")
        print()                   
                    

matmul()





