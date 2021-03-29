class CreditCard:
    
    
    def __init__(self, customer, bank, acnt, limit):
        
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0
        
    def getcustomer(self):

        return self.customer
    
    def getbank(self):
        
        return self.bank

    def getaccount(self):
        
        return self.account

    def getlimit(self):
        
        return self.limit

    def getbalance(self):
    
        
        return self.balance
    
    def charge(self, price):
        
        if price + self.balance > self.limit:
            return False 
        else: 
            self.balance += price
            return True
    
    def makepayment(self,amount):
        
        self.balance = self.balance - amount
        return self.balance
    


if __name__ == "__main__":
    wallet=[]
    wallet.append(CreditCard("John Bowman" , "California Savings" ,5391037593875309 ,2500))
    wallet.append(CreditCard("John Bowman" , "California Federal" ,3485039933951954 ,3500))
    wallet.append(CreditCard("John Bowman" , "California Finance" ,5391037593875309 ,5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =',wallet[c].getcustomer())
        print('Bank = ',wallet[c].getbank())
        print('Account = ',wallet[c].getaccount())
        print('Limit = ',wallet[c].getlimit())
        print('Balance = ', wallet[c].getbalance())
        while wallet[c].getbalance() > 100 :
             wallet[c].makepayment(100)
             print('New balance = ',wallet[c].getbalance())
        print()
