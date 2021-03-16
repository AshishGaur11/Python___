from array import *

def go(A):

    A = array('i',[])
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter the value\n"))
        A.append(w)
    
    center(A,0,len(A)-1)
    
    print("here are your values\n")
    for o in range(len(A)):
        print(A[o])
    
go(A)

def center( A, low, high) :
    
    if low<high :
        j = partition(A, low,high)
        center(A, low,j-1)
        center(A, j+1,high)
    
center()

def partition( A, l, h):

    
    i=l+1
    j=h
    p=A[l]
    while i<j :
    
        while A[i]<p :
            i = i + 1
        while A[j]>p :
            j = j + 1
        
        if i<j :
        
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
        
    
    temp=A[l]
    A[l]=A[j]
    A[j]=temp
    return j
















from array import *

def go(A=[]):

    A = array('i',[])
    n = int(input("Enter the length of array\n"))
    for q in range(n):
        w = int(input("Enter the value\n"))
        A.append(w)
    
    center(A=[],0,len(A)-1)
    
    print("here are your values\n")
    for o in range(len(A)):
        print(A[o])
    
go(A)

def center(A=[], low, high) :
    
    if low<high :
        j = partition(A, low,high)
        center(A, low,j-1)
        center(A, j+1,high)
    
center()

def partition( A=[], l, h):

    
    i=l+1
    j=h
    p=A[l]
    while i<j :
        while A[i]<p :
            i=i+1
        while A[j]>j :
            j=j+1
        if i < j:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
            
    temp=A[l]
    A[l]=A[j]
    A[j]=temp
    return j
     
     
