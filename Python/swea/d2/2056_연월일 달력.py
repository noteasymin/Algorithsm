def solution():
    d = input()
    # d is 22220228
    validDate(d)


def validDate(d, test_case):

    month = int(d[4:6])
    day = int(d[6:8])
    if month < 1 or month > 12:
        print(-1)
        return
    if month == 2:
        if day < 1 or day > 28:
            print(-1)
            return
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 1 or day > 30:
            print(-1)
            return
    else:
        if day < 1 or day > 31:
            print(-1)
            return
    print('#' + test_case + d[:4] + "/" + d[4:6] + "/" + d[6:8])
