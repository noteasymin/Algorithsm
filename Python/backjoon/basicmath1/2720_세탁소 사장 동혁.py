def solution():
    t = int(input())

    for i in range(t):
        quarter = 0
        dime = 0
        nickel = 0
        penny = 0
        money = int(input())

        if money >= 25:
            quarter = money // 25
            money -= quarter * 25

        if money >= 10:
            dime = money // 10
            money -= dime * 10

        if money >= 5:
            nickel = money // 5
            money -= nickel * 5

        if money >= 1:
            penny = money // 1
            money -= penny * 1

        print(quarter, dime, nickel, penny)


solution()
