class SavingsAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance
    
    def add_interest(self):
        self._balance += self._balance * 0.05
        return self._balance

s1 = SavingsAccount(1000)
print(s1.add_interest())
