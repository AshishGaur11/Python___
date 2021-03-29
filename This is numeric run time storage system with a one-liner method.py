#code STARTs HERE
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
    
def search():
    
    print("enter the value for search\n")
    a = 0
    s = int(input())
    while True:
        a = a+1
        if c[0]==s:
            print("found at 1 th position")
            break
        elif c[a]==s:
            print("found at",a+1,"th position")
            break
    main()
    
def main():
    
    print("\nPress the value to perform those functions in down there--\n")
    print("0 for Enter in oneshot")
    print("1 for insert")
    print("2 for remove")
    print("3 for display")
    print("4 to search")
    print("press q & Enter\n")
    n = input()
    while n != '5'  :
        
        if n == '0':
            go()
        elif n == '1':
            push()
        elif n== '2':
            pop()
        elif n== '3':
            display()
        elif n== '4':
            search()
        elif n == 'q':
            print("Hope your expireance was good!!")
            break
        else :
            print("sorry does'nt work")
            main()
        break
        
main()

# This is a one liner for compressed versions to deploy!!
exec("""\nc = []\n\ndef go():\n    \n    w = int(input("Enter values\\n"))\n    c.append(w)\n    main()\n        \ndef push():\n    \n    n = int(input("Enter the position\\n"))\n    w = int(input("Enter values\\n"))\n    c.insert(n,w)\n    main()\n    \ndef pop():\n    \n    print("press 1 for remove by position or press 2 for by object\\n")\n    x = int(input())\n    if x==1 :\n        m = int(input("Enter the position\\n"))\n        c.pop(m)\n    elif x==2:\n        t = int(input("Enter the Object\\n"))\n        c.remove(t)\n    else:\n        main()        \n        \n    main()\n    \ndef display():\n    \n    print("here are your values\\n")\n    for o in range(len(c)):\n        print(c[o])\n    main()\n    \ndef search():\n    \n    print("enter the value for search\\n")\n    a = 0\n    s = int(input())\n    while True:\n        a = a+1\n        if c[0]==s:\n            print("found at 1 th position")\n            break\n        elif c[a]==s:\n            print("found at",a+1,"th position")\n            break\n    main()\n    \ndef main():\n    \n    print("\\nPress the value to perform those functions in down there--\\n")\n    print("0 for Enter in oneshot")\n    print("1 for insert")\n    print("2 for remove")\n    print("3 for display")\n    print("4 to search")\n    print("press q & Enter\\n")\n    n = input()\n    while n != '5'  :\n        \n        if n == '0':\n            go()\n        elif n == '1':\n            push()\n        elif n== '2':\n            pop()\n        elif n== '3':\n            display()\n        elif n== '4':\n            search()\n        elif n == 'q':\n            print("Hope your expireance was good!!")\n            break\n        else :\n            print("sorry does'nt work")\n            main()\n        break\n        \nmain()\n""")
