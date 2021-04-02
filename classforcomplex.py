


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
        return self.x,self.i
    
    def __add__(self,other):
        return complex(self.x + other.x, self.i + other.i)
        
        
        
if __name__ == "__main__":
    complex.get(a)
    complex.get(b)
    c = a + b
    complex.put(c)
    
    
    #this is better
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
        return self.x,self.i
    
    def __add__(self,other):
        self.x = self.x + other.x
        self.x = self.i + other.i        
        
        
if __name__ == "__main__":
    complex.get(a)
    complex.get(b)
    c = a + b
    complex.put(c)
    
  #or 
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
        return self.x,self.i

    def __add__(self,r,e):
        self.x = r.self.x + e.self.x
        self.i = r.self.i + e.self.i

        
        
if __name__ == "__main__":
    complex.get(a)
    complex.get(b)
    c = a + b
    complex.put(c)
