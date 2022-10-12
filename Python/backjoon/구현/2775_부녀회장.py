T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    h = 0
    for i in range(n+1):
        h += i

    print(h)