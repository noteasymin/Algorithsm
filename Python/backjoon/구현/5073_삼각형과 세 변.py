while True:
    lst = list(map(int, input().split()))
    a = lst[0]
    b = lst[1]
    c = lst[2]

    lst = sorted(lst,reverse=True)

    if a == 0 and b == 0 and c == 0:
        break
    elif lst[0] >= lst[1] + lst[2]:
        print('Invalid')
    elif a == b and b == c and c == a:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')