T = int(input())

lst = [0, 1]
cnt = 2

for i in range(40):
    lst.append(lst[cnt-2] + lst[cnt-1])
    cnt += 1

for i in range(T):
    N = int(input())

    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(lst[N-1],lst[N])