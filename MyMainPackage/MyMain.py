from myBank import Bank
from Test import *
from MyMainPackage.HelloWorld import *

bank=Bank(1000)
bank._Bank__balance=2000000000

print(bank.getbalance())
bank.setbalance(100000)
print(bank.getbalance())
bank.depoite(10000)
print(bank.getbalance())
print(bank.getbalance())
print(bank.__dict__)

print(getbalance())
setbalance(100)
balance=1000
print(getbalance())
depoite(10)
print(getbalance())
