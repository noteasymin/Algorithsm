while True:
    num = int(input())

    if num == 0:
        break

    if len(str(num)) % 2 == 0:
        temp = list(str(num))
        if list(str(num)) == list(temp.__reversed__()):
            print('yes')
        else:
            print('no')

    else:
        del list(str(num))[len(list(str(num))) // 2]
        temp = list(str(num))
        if list(str(num)) == list(temp.__reversed__()):
            print('yes')
        else:
            print('no')