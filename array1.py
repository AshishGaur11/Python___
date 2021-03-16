from array import *
"""The most important thing is python supports this unique property that allows us to use 2 different feature 
 at the same time 
 first THERE IS NO FIXED SIZE OF AN ARRAY
 second YOU CAN USE IN DYNAMIC MEMORY ALLOCATION """

def main():

    a = array('i',[40,43,4,23,423,23,8])
    a.reverse()
    print(a.buffer_info())
    for r in range(7): # non dynamic
        print(a[r],end= " ")
    for i in a :  # dynamic
        print(i,end= "\n ")
    for e in range(len(a)) : # dynamic
        print(a[e],end= " ")

    b = array(a.typecode, (m for m in a)) # here we are taking value from k and copying into b
    for f in range(len(b)) :
        print(b[f])


main()