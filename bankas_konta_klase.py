class BankAccount():
    def __init__(self,owner, balance, account_type,):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        
        
    def deposit(self,amount):
       self.balance = self.balance + amount
       return self.balance
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        
        


    





        