T = int(input())

for i in range(T):
    n = int(input())
    cnt = len(bin(n))-3
    lst = []

    for j in (bin(n)[2:]):
        if j == '1':
            lst.append(str(cnt))
        cnt -= 1

    print(' '.join(lst[::-1]))