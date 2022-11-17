T = int(input())
c = 1
def solution():
    N = int(input())
    global c
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    cnt = []
    for i in money:
        if N >= i:
            a = N // i
            cnt.append(a)
            N = N - a * i
        else:
            cnt.append(0)

    print(f'#{c}')
    c += 1
    for i in cnt:
        print(i,end=" ")
    print()

for _ in range(T):
    solution()