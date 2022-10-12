def check_price():
    enter_price = int(input())
    up = '(↑)'
    low = '(↓)'
    same = '(=)'

    if enter_price > price:
        print(str(enter_price)+ up)
    elif enter_price == price:
        print(str(enter_price) + same)
    else:
        print(str(enter_price) + low)

    return enter_price

def buy():
    while True:
        reasonable_price = int(input())

        if market_price <= reasonable_price:
            print('구매')
            break
        else:
            print('가격이 적당하지 않음')
            continue

price = 1000

enter_price = check_price()

market_price = (price + enter_price) // 2

buy()