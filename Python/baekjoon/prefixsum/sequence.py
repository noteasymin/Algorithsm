import sys


def solution():
    input = sys.stdin.readline
    N, K = map(int,input().split())

    arr = list(map(int, input().split()))
    ismax = 0
    if K == 1:
        print(max(arr))
    elif N == K:
        print(sum(arr))
    else:
        for i in range(N-K+1):
            if sum(arr[i:K+i]) > ismax:
                ismax = sum(arr[i:K+i])

    print(ismax)

solution()

