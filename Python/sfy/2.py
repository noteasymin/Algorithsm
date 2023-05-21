def check_1(a, N):
    N = N // 2
    for i in range(N):
        if N == 0:
            if N % 2 == 0:
                continue
            else:
                return 0

        if a[N * 2] % 2 == 0:
            continue
        else:
            return 0

    print('pass')


def check_2(a, N):
    N = N // 2
    for i in range(N):
        if N == 0:
            if N % 2 == 1:
                continue
            else:
                return 0

        if a[N * 2] % 2 == 1:
            continue
        else:
            change_1(a, )

    print('pass')

def change_1(a,index):
    global times

    temp = a[index]
    a[index] = a[index+1]
    a[index+1] = temp

    times += 1

    if a[0] % 2 == 0:
        check_1(a,len(a))
    else:
        check_2(a,len(a))

def solution():
    global cnt
    N = int(input())
    num_lst = list(map(int, input().split()))


T = int(input())
times = 0
cnt = 1
times = 1


for _ in range(T):
    solution()
