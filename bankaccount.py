class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(
                f"Success! {self.owner} deposited {amount}. New balance: {self._balance}"
            )
        else:
            print("Please input valid amount")

    def withdraw(self, withdraw_amount):
        if 0 < withdraw_amount <= (self._balance - self.MIN_BALANCE):
            self._balance -= withdraw_amount
            print(f"Success! {self.owner} withdrew {withdraw_amount}.")
        else:
            print("Transaction Denied: Insufficient funds or invalid amount.")
            print(f"Note: You must maintain a minimum balance of {self.MIN_BALANCE}.")

    def __str__(self):
        return f"Account owner: {self.owner} | Avalible balance: {self._balance} "

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


bankaccount1 = BankAccount("Aye Aye", 5000)
bankaccount1.deposit(900)
print(bankaccount1)
bankaccount1.withdraw(1200)
print(bankaccount1)
print(bankaccount1.is_valid_interest_rate(10))

bankaccount2 = BankAccount("Thu Thu", 6500)
bankaccount1.deposit(500)
print(bankaccount2)
bankaccount2.withdraw(6990)
print(bankaccount2)
print(bankaccount2.is_valid_interest_rate(4))
