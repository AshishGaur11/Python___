c = []
def go():
    w = int(input("Enter values\n"))
    c.append(w)
    main()
        
def push():
    
    n = int(input("Enter the position\n"))
    w = int(input("Enter values\n"))
    c.insert(n,w)
    main()
    
def pop():
    
    print("press 1 for remove by position or press 2 for by object\n")
    x = int(input())
    if x==1 :
        m = int(input("Enter the position\n"))
        c.pop(m)
    elif x==2:
        t = int(input("Enter the Object\n"))
        c.remove(t)
    else:
        main()        
        
    main()
    
def display():
    
    print("here are your values\n")
    for o in range(len(c)):
        print(c[o])
    main()
    
def main():
    
    print("\nPress the value to perform those functions in down there--\n")
    print("0 for Enter in oneshot")
    print("1 for insert")
    print("2 for remove")
    print("3 for display")
    print("4 to quit\n")
    n = int(input())
    while n != 5  :
        
        if n == 0:
            go()
        elif n == 1:
            push()
        elif n== 2:
            pop()
        elif n== 3:
            display()
        elif n== 4:
            print("Hope your expireance was good!!")
            break
        else :
            print("bye")
        break
        
main()


            
    

