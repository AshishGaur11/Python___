# a = b * q + r
def qwer(a,b):
    
    if a > b:
        q=0
        r=0
        while True :
            q=a//b
            r=a%b
            a=b
            b=r
            print(b)
