class Account:
    intetest = 0.3

    def __init__(self, holder):
        self.holder = holder
        self.balance = 100

    def get_balance(self):
        return self.balance

    def set_balance(self, value):
        self.balance = value

    def update(self):
        self.intetest += 0.1
        return self.intetest

    # create the private method by adding two underscores before function name
    def __withdraw(self, amount):
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    John = Account('John')
    print(f"before: {John.intetest}")
    Account.intetest = 0.4
    print(f"after the class update: {John.intetest}")
    print(f"after the instance update: {John.update()}")

    #  left = John.__withdraw(70)  # Error

    # invoke the private method by adding the class name
    left = John._Account__withdraw(70)  # Success
    print(f"left money: {left}")

