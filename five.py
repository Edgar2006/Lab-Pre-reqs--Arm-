class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,num):
        self.balance += num
    def withdraw(self,num):
        self.balance -= num
    def get_balance(self):
        return self.balance
        
        
# Create a bank account with an initial balance of $100 
account = BankAccount("123456789", 100.0) 
# Deposit $50 
account.deposit(50.0) 
# Withdraw $30 
account.withdraw(30.0) 
# Get the current balance 
balance = account.get_balance() 
print(f"Current balance: ${balance}")