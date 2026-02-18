class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            result = f"Withdrawal successful. Remaining balance: {self.__balance}"
        else:
            result = f"Insufficient funds. Balance remains: {self.__balance}"
        
        print(result)
        return result

acc = BankAccount(1000)
acc.withdraw(200)
acc.withdraw(900)
