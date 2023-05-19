N = int(input())
cnt = N-1
for i in range(1, N + 1):
    print(' ' * (cnt) + '*' * (2*i-1))
    cnt = cnt - 1

cnt = 1
for i in range(N-1, 0, -1):
    print(' ' * cnt + '*' * (2*i-1))
    cnt = cnt + 1