def solution():
    check = []

    a = int(input())
    if a not in check:
        check.append(a)

    b = int(input())
    if b not in check:
        check.append(b)

    c = int(input())
    if c not in check:
        check.append(c)

    if (a + b + c == 180) & (len(check) == 1):
        print('Equilateral')

    elif (a + b + c == 180) & (len(check) == 2):
        print('Isosceles')

    elif (a + b + c) == 180:
        print('Scalene')

    else:
        print('Error')


solution()
