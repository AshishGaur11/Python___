def ditw(*arg):    
    m = [None]*len(arg)
    for i in range(0, len(arg)):    
        m[i] = arg[i] 
    m.sort()
    print(m)
