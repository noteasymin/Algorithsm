def cacl():
    cnt = int(input())
    money = []
    for i in range(cnt):
        money.append(int(input()))
        if money[-1] == 0:
            del money[-1]
            del money[-1]
    print(sum(money))

cacl()