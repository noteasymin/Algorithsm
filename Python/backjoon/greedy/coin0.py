import sys
input = sys.stdin.readline


def solution():
    N, K = map(int,input().split())
    N_lst = []
    cnt = []
    for i in range(N):
        N_lst.append(int(input()))

    N_lst.sort(reverse=True)

    for i in range(len(N_lst)):

        cnt.append(K // N_lst[i])
        K -= cnt[i] * N_lst[i]


    print(sum(cnt))
solution()