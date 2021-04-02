



class complex:

    def __init__(self,x,i):
        self.x = x
        self.i = i
    
    def get(self):
        self.x = int(input("enter real number"))
        self.i = int(input("enter complex number"))

    def put(self):
        print(self.x,'+',self.i,'i')

    def __mul__(self,other):
      return complex(self.x * other.x, self.i * other.i)
    
    def __add__(self,other):
      return complex(self.x + other.x, self.i + other.i)
  
if __name__ == "__main__":
    a = complex(0,0)
    b = complex(0,0)
    c = complex(0,0)
    d = complex(0,0)
    complex.get(a)
    complex.get(b)
    c = a * b
    d = a + b
    complex.put(c)
    complex.put(d)
    
    
***********************************************************************************************************
