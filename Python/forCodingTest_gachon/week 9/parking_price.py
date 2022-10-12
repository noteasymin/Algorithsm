import math


def solution(fees, records):
    default_time = fees[0]
    default_price = fees[1]
    unit_time = fees[2]
    unit_price = fees[3]

    current_car = {}
    account_book = {} # answer
    platenumber = 0
    time = 0

    for i in records:
        time = i[0:5]
        platenumber =i[6:10]
        car = [time,platenumber]

        if i[11:] == 'OUT':
            if platenumber not in account_book:
                account_book[platenumber] = (((int(i[0:2])*60) + (int(i[3:5]))) - (int(current_car[platenumber][0:2]) * 60 + int(current_car[platenumber][3:5])))

            elif platenumber in account_book:
                account_book[platenumber] += (((int(i[0:2])*60) + (int(i[3:5]))) - (int(current_car[platenumber][0:2]) * 60 + int(current_car[platenumber][3:5])))

            del current_car[platenumber]


        elif i[11:] == 'IN':
            current_car[platenumber] = time

    if len(current_car) != 0:
        for i in current_car:
            if i in account_book:
                platenumber = i
                account_book[platenumber] += ((23 * 60) + 59) - (int(current_car[platenumber][0:2]) * 60 + int(current_car[platenumber][3:5]))
            else:
                platenumber = i
                account_book[platenumber] = ((23 * 60) + 59) - (int(current_car[platenumber][0:2]) * 60 + int(current_car[platenumber][3:5]))

    new_account_book = []
    for i in account_book:
        new_account_book.append([i,account_book[i]])

    new_account_book = sorted(new_account_book)

    answer = []
    for i in new_account_book:
        if i[1] <= default_time:
            answer.append(default_price)
        else:
            answer.append(default_price + math.ceil((i[1] - default_time)/unit_time) * unit_price)

    print(answer)

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
solution(fees,records)

#012345678910111213
#05:34 5961   I N T