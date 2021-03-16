def main():


    print("enter the cloths type\n")
    a = int(input("press 1 for cloth1, press 2 for cloth2 \n"))
    if a==1 :
        print("enter the purchasing amount\n")
        b = int(input())
        if b<=1000 :
         f = b
        elif b >= 1001 and b <= 2000 :
         f = b-b*0.05
        elif b >= 2001 and b <= 3000 :
         f = b-b*0.075
        elif b >= 3001 and b <= 4000 :
         f = b-b*0.1
        elif b >= 4001 and b <= 5000 :
         f = b-b*0.12
        else:
         f=b-b*0.15
    
    elif a==2 :
        print("enter the purchasing amount\n")
        b = int(input())
        if b <= 1000 :
         f = b-b*0.05
        elif b >= 1001 and b <= 2000 :
         f = b-b*0.075
        elif b >= 2001 and b <= 3000 :
         f = b-b*0.1
        elif b >= 3001 and b <= 4000 :
         f = b-b*0.12
        elif b >= 4001 and b <= 5000 :
         f = b-b*0.15
        else:
         f= b-b *0.2
    elif a is None or a>2 or a==0:
        print("invalid option")
    print(f,"this is your discount")

main()
