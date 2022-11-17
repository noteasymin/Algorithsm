N, M = map(int, input().split())
if N <= M:
    print(abs(N-M))
else:
    print(abs(M-N))