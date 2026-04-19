class BankAccount:
    def __init__(self,Account_Number,Balance):
        self.Account_Number = Account_Number
        self.Balance = Balance

    def deposit(self, amount):
        if amount >0 :
            self.Balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposited amount must be positive")

    def withdraw(self,amount):
        if amount > self.Balance:
            print("Insufficient funds")
        elif amount <= self.Balance:
            self.Balance -= amount 
            print(f"Withdrew {amount}")

    def get_balance(self):
        print(f"Current balance is {self.Balance}")
        # return self.Balance
    
account1 = BankAccount(123456789, 0)
account1.deposit(2000000)
account1.withdraw(50000)
account1.get_balance()
