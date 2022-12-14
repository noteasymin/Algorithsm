T = int(input())

for i in range(T):
    a, b = map(str, input().split())
    a = int(a) - 1

    b = list(b)
    del b[a]

    print(''.join(b))