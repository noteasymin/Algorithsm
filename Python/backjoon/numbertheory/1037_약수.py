def solution():
    N = int(input())

    N_lst = list(map(int, input().split()))

    print(max(N_lst) * min(N_lst))

solution()