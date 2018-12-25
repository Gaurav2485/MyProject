class Bank:

    # constructor
    def __init__(self, balance):
        self.__balance = balance

    # Check balnace
    def getbalance(self):
        return (self.__balance)

    # Modify balance
    def setbalance(self, balance):
        self.__balance = balance

    # Deposte
    def depoite(self, amount):
        if self.__balance > -amount:
            return (self.__balance + amount)
        else:
            return "bye"

    # Withdraw
    def withdraw(self, amount):
        if self.__balance > amount:
            return (self.__balance - amount)



    print(__name__+"Hello")
# if __name__=="__main__":
