for i in range(3):
    lst = list(map(int, input().split()))

    result = lst.count(0)

    if result == 1:
        print('A')
    elif result == 2:
        print('B')
    elif result == 3:
        print('C')
    elif result == 4:
        print('D')
    else:
        print('E')