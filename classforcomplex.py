


class complex:

    def __init__(self,x,i):
        self.x = x
        self.i = i
        
    def get(self):
        self.x = int(input("enter real number"))
        self.i = int(input("enter complex number"))
        
    def put(self):
        print(self.x,'+',self.i,'i')
    
    def __str__(self):
        return 'complex (%d, %d)' % (self.x, self.i)

    def __add__(self,other):
        return complex(self.x + other.x, self.i + other.i)
        
        
        
if __name__ == "__main__":
    complex.get(a)
    complex.get(b)
    c = a + b
    complex.put(c)
    
