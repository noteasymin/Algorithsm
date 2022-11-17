def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다. ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print ("출금이 완료되었습니다 잔액은 {0}원입니다. ".format(balance-  money))
        return balance - money
    else:
         print ("출금이 완료되지 않았습니다 잔액은 {0}원입니다. ".format(balance))
         return balance

def withdraw_night(balance, money):
    commision = 100
    return commision, balance - money - commision
balance = 10000
balance = withdraw(balance, 500)
