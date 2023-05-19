N = int(input())
cnt = N
for i in range(N):
    print(' ' * i + '*' * (2 * cnt - 1))
    cnt -= 1

cnt = 2
for i in range(N-1,0,-1):
    i = i-1
    print(' ' * i + '*' * (cnt*2-1))
    cnt += 1