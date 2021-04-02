



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



#one for the vectors
class Vector:
   
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def put(self):
        print(self.a,self.b)

     def __add__(self,other):
         return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,2)
v3 = v1 + v2
Vector.put(v3)








*************************************************************************************************
class complex:

    def __init__(self,x,i):
        self.x = x
        self.i = i
    
    def get(self):
        self.x = int(input("enter real number"))
        self.i = int(input("enter complex number"))

    def put(self):
        print(self.x,'+',self.i,'i')

    def __add__(self,other):    #for long process!!
        v = self.x + other.x
        w = self.i + other.i
        return complex(v,w)
    
    def __mul__(self,other):
        return complex(self.x * other.x, self.i * other.i)
        
  
if __name__ == "__main__":
    a = complex(0,0)
    b = complex(0,0)
    c = complex(0,0)
    d = complex(0,0)
    complex.get(a)
    complex.get(b)
    c = complex.__add__(a,b) # both give you the value
    c = a + b # both give you the value & one one value appere on screen !!!
    d = a * b
    complex.put(c)
    complex.put(d)
  
