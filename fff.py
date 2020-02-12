class Invalidfund(Exception):
    def  __init__(self,kabir_singh):
        self.msg=kabir_singh

a=int(input("Amount to withdraw:"))
Bank_balance=1000
try:
    if a>Bank_balance:
        raise Invalidfund("Work hard for more money.You lazy")
except Invalidfund as Do:
    #print(Do.msg)
else:
    print("Your withdraw money is",a)
    print("Your remainning Bank balance is",Bank_balance-a)
print("Over")
