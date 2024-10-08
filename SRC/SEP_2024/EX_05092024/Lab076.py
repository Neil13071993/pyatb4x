class Bank:
    def __init__(self, __account_number, balance):
        self.balance = balance
        self.__account_number = __account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("not allowed")

    def internal_method(self):
        print("private_method")
        print(self.__account_number)
        self.show_me_account_number()



icici = Bank(123456789,100)
icici.deposit(100)
icici.check_balance()
print(icici.show_me_account_number(True))
icici.deposit(100)
icici.check_balance()