from Account import Account  # Fix 2 & 3: was 'Accounts' (wrong class name)

class CurrentAccount(Account):  # Fix 3: was CurrentAccount(Accounts)
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    # Polymorphism: Different implementation of withdraw
    def withdraw(self, amount):
        available_funds = self.get_balance() + self.overdraft_limit  # Fix 4: was 'avaliable_funds' (typo)
        if 0 < amount <= available_funds:
            # Use the parent's withdraw if within actual balance,
            # otherwise handle overdraft manually
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                overdraft_used = amount - self.get_balance()
                super().withdraw(self.get_balance())  # drain balance to 0
                print(f"Overdraft of ${overdraft_used:.2f} used. Balance is now $0.")
            print(f"Withdrawal of ${amount} approved (using overdraft if necessary).")
        else:
            print("Withdrawal denied: exceeds overdraft limit.")


print("\n--- Current Account ---")
current = CurrentAccount("Bob", 100)
current.withdraw(400)