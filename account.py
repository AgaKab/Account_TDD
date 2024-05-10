class Account:
    def __init__(self, amount=0):
        self.saldo = amount
    
    def deposit(self, cash):
        if cash > 0:
            self.saldo += cash
        else:
            raise ValueError("Desposit can't be negative!")
        
    def withdraw(self, cash):
        if self.saldo >= cash:
            self.saldo -= cash
        else:
            raise ValueError("Not enought money!")
              
    def get_balance(self):
       return self.saldo
        
    
    