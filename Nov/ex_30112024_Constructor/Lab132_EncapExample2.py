class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance  # Public
        self.__account_number = account_number  # Private


    def check_balance(self):
        print(self.balance)


    def deposit(self, amount):
        self.balance = self.balance + amount


    def show_me_account_number(self):
        print(self.__account_number)

icici = Bank( 123456, 1000)
icici.deposit(100)
icici.check_balance()
print(icici.balance)

icici.show_me_account_number()
