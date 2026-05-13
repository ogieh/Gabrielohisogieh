from Account import Account  

class SavingsAccount(Account):  
    def __init__(self, owner, balance=0, interest_rate=0.02, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  
        self.withdrawal_limit = withdrawal_limit

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate  
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")

    def withdrawal(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal denied: Savings account limit is ${self.withdrawal_limit}")
            return
        super().withdraw(amount) 


print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
savings.withdrawal(100)    
savings.apply_interest()