#global
myStack = []
myStackFilledElements = 0 #this is how many elements are filled
myMaxStackSize = 10

def main():
    outputString = ""
    #iterates through the expression
    expressionList = getInputExpression()

    for exp in expressionList:
        
        #if it's letter or number
        if (exp.isalpha() or exp.isdigit()):
            outputString += exp
        
        #If it's an OPERATOR
        elif ((exp == '+') or (exp == '-') or (exp == '*') or (exp == '/') or (exp == '^')):
            if (isMyStackEmpty() == True):
                myStackPush(exp)
                
            else:
                #is the current exp less than or equal to the top of the store priority
                while ((checkPriority(exp) == "expLower")): #top has higher priority and stack not empty
                    if (isMyStackEmpty() == True): #after it popped, the stack became empty and operator is pushed
                        myStackPush(exp)
                        
                    else: #Stack NOT empty
                        outputString += myStackPop()
                
                if ((isMyStackEmpty() == True) or (checkPriority(exp) == "topLower")): #have to check again after pops, very repetitive
                    myStackPush(exp)
                    
        #If it's a LEFT '('
        elif (exp == "("):
            myStackPush(exp)
            
        #If it's a RIGHT ')'
        elif (exp == ")"):
            while ((isMyStackEmpty() == False) and (myStack[getMyStackLastIndex()] != "(")):
                outputString += myStackPop() #returned the popped item
            #if it IS a left paren:
            myStackPop() #pops the left paren without printing it            
    
    while (len(myStack) > 0):
        outputString += myStackPop()
    
    
    #Final Answer:
    print("Your espression in postfix form:", outputString)                  


def getInputExpression():
    #global myStackFilledElements 
    inputExpression = input("Enter an equation in infix form: ")
    inputExpression = inputExpression.replace(" ", "")
    expressionList = list(inputExpression)
    return expressionList

def isMyStackEmpty():
    if myStackFilledElements == 0:
        return True #yes, it is empty
    else:
        return False #myStack is not empty
    
def myStackPush(expression):
    #global myStack
    global myStackFilledElements
    if (myStackFilledElements < myMaxStackSize+1): #+1 bc 10 is size, 11 is index
        myStack.append(expression)
        myStackFilledElements += 1
       
    else:
        print("Expression cannot be pushed because the stack is full")

def checkPriority(exp): #if this expression has lower priority than top of stack return false
    if (isMyStackEmpty() == False):
        topOperator = myStack[getMyStackLastIndex()] #item in the top/last index of the stack
        
        topOperatorPriority = operatorPriority(topOperator)
        presentOperatorPriority = operatorPriority(exp)
        
        if (presentOperatorPriority <= topOperatorPriority):
            return "expLower"
        else:
            return "topLower"
    
    
def operatorPriority(operator):
    if operator == '(':
       priority = 0
    elif operator == '+' or operator == '-':
       priority = 1
    elif operator == '*' or operator == '/':
       priority = 2
    return priority
    
    
def getMyStackLastIndex():
    index = myStackFilledElements - 1
    return index

def myStackPop():
    global myStackFilledElements
    if (isMyStackEmpty() == False): #it's not empty
        
        poppedElement = popIt()
        myStackFilledElements-=1#decrease index after item has been popped
        
        return poppedElement
    else:
        print("The stack is empty and cannot be popped.")

def popIt():
    return myStack.pop(getMyStackLastIndex())

main()





