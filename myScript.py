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

# we 
def mac(q1,q2):
    v = 1
    
    for noe in range(0,q2):
        v = v * q1
        print(noe)
    print(v)

mac(2,344344)


weq = 22/7
print(weq)
        


x = [2]
y = x
print(x is y)


def sum():
    er = int(input("give 1"))
    me = int(input("give 2"))
    print(me + er)

def goodtogo(doit):
    doit()

goodtogo(sum)

mew = open('mac.txt', '+a')  

mew.write('this is waht seems like')



def rest(c,d):
    a = c+d
    print(a)

rest(33,44)


import math

def square(x):
    result = []
    for y in x:
        result.append(math.pow(y,2.0))
    return result 

print(square([1,2,3]))




    
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



aeeeeeee = [1,12,3,43,443,5,46,546,33,7,8,89,89]
aeeeeeee.sort()
print(aeeeeeee)

def calculateTotalSum(*arguments):
    totalSum = 0
    for number in arguments:
        totalSum += number
    print(totalSum)
 

def sum(m):
    i = 0
    while m != 0 :
        x = m % 10
        i = i + x
        m = m // 10

    print("\n")
    return i


def digital_root(n):
    x = str(n)
    r = 0
    while len(x) > 1:
        r = 0
        for i in range(len(x)):
            r = r + int(x[i])
        x = str(r)
    return r

    
def dit(*arg):
    arg = []

    arg.sort()
    print(arg)




def addition(n):
    return n * n
  

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


def ditw(*arg):    
    d = [None]*len(arg)
    for i in range(0, len(arg)):    
        d[i] = arg[i] 


def qwe(*argq):    
    alist = [None]*len(argq)
    for i in range(0, len(argq)):    
        alist[i] = argq[i] 
    mergeSort(alist)
    


def mergeSort(alist):
    
    print("Splitting: ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

    print(alist)




def qwe(*argq):    
    alist = [None]*len(argq)
    for i in range(0, len(argq)):    
        alist[i] = argq[i] 
    c = len(alist)
    q = 0
    d = 0
    for f in range(c):
        x = alist[f]
        if x.isalpha() :
            q = q+1
        elif x.isdigit() :
            d = d+1
    print("numbers of alpha",q)
    print("numbers of digit",d)


qwe("45","4343","gre","46") 


    
 
a = 'fsdfsdf'

if a.isalpha() :
    print("is a alpha")
elif a.isdigit() :
    print("is a digit")


#**************************************************************************************

        
        
def qwe(*opse): 
    ops = [None]*len(opse)
    for i in range(0, len(opse)):    
        ops[i] = opse[i]    
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))

        return sum(stack)


def asd(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    if arr(n / 2) < arr((n / 2) - 1):
        return asd(arr[:n / 2])
    if arr(n / 2) < arr((n / 2) + 1):
        return asd(arr[n / 2:])
    return arr[n / 2]




def calPoints(ops):
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'c':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'd':
            stack.append(2 * stack[-1])    
        else:
            stack.append(int(op))
    
    return sum(stack)

if __name__=='__main__':
    line = input()
    ops = line.strip().split()
    print(ops)

    print(calPoints(ops))




#1. MIT first Algo peak finding 

def asd(arr):
  n = len(arr)
  if n == 1:
    return arr[0]
  if n == 2:
    return max(arr)
  if arr[n // 2] < arr[(n // 2) - 1]:
    return asd(arr[:n // 2])
  if arr[n // 2] < arr[(n // 2) + 1]:
    return asd(arr[n // 2:])
  return arr[n // 2]

asd([34,3,4,3,4,3])

# this is for Mat
def sdf(plane):
    n = len(plane)
    middle_row = plane[n // 2]
    middle_max = max(middle_row)
    i = middle_row.index(middle_max)
    if n == 1:
        return middle_max
    if n == 2:
        return max(plane[0][i], middle_max)
    if middle_max < plane[(n // 2) - 1][i]:
        return sdf(plane[n // 2:])
    if middle_max < plane[(n // 2) + 1][i]:
        return sdf(plane[:n // 2])
    return middle_max

sdf([[54,45,54],[98,7,878],[787,6,8]])  

    
def sol(x):
    c = 0
    while x!=0:
        c = c*10 + x%10
        x=x//10
    return c

l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)


def qwe(rr,t):
    c = 0
    p = len(rr)
    for i in range(p):
        for j in range(p):
            if rr[i] == t:
                c=c+1
            elif rr[i] + rr[j] == t:
                c=c+1
    if c == 0:
        print("not found")
    else:
        print("found")

weeq = [-1,0,1,2,3,4,5,6,7,8,9,10]
print(weeq)
print(weeq[4:],"all after pos 4th")
print(weeq[:4],"all before pos 4th")
print(weeq[:-4],"all after pos -4th")
print(weeq[-4:],"all before pos -4th")


a = bool()
b = bool()
c = bool()
a = False
b = False
c = True
if c == a and b:
    print(c,"1")
if c == a or b:
    print(c,"2")
else :
    print(c,"3")

           

def qwe(rr,t):
    c = 0
    p = len(rr)
    for i in range(p):
        for j in range(p):
            if rr[i] + rr[j] == t:
                r = i
                e = j
    return e,r

    
