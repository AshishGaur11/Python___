def ditw(*arg):    
    m = [None]*len(arg)
    for i in range(0, len(arg)):    
        m[i] = arg[i] 
    m.sort()
    print(m)
    
    
    
    
def addition(n):
    return n * n
  

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
