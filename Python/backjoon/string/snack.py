import sys
def remain():
    price, cnt, money = map(int,sys.stdin.readline().split())
    total = price * cnt

    if total > money:
        print(abs(money - total))
    else:
        print(0)

remain()