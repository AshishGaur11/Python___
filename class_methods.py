class vehicle:
    
    def WannaASK():
        
        c=int(input("does it have wheels if how many \n"))
        if c==4 :
            print("its a car")
            car()
        elif c==2 :
            print("its a bike")
            bike()
        elif c==0 :
            print("there was nothing!")
        else:    
            print("good bye")
        
def car():
    print("car has 4 wheels")
    print("it has 2 somtimes 4 doors\n")
    print("        ///=========\          ")
    print("     -------------------------      ")
    print("     --O------------------O----     ") 
        
def bike():
    print("bike has a 2 wheels\n")
    print("        O           ")
    print("    =========       ")
    print("     O     O        ")            

        
        
v = vehicle
v.WannaASK()
