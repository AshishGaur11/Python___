def main():
    print("enter the units")
    n = int(input())
    if n <= 100 :
        a = 250
    elif n >= 100 and n <= 200:
        a=(n-100)*3+250
    elif n >= 201 and n <= 300:
        a=(n-200)*5+550
    elif n >= 301 and n <= 400:
        a=(n-300)*7+1050
    else:
        a=(n-400)*9+1750
    print(a)
main()