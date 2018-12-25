''' This program is used to commmute the
bank account
and my first program too'''

balance=0


def getbalance():
    print("HelloWorld1")
    return (balance)


# Modify balance
def setbalance(ibalance):
    global balance
    balance = ibalance
    print("HelloWorld1")



# Deposte
def depoite(amount):
    global balance
    if balance > -amount:
        balance =balance + amount
    else:
        return "bye"


# Withdraw

def withdraw( amount):
    if balance > amount:
        return (balance - amount)


print(__name__)
