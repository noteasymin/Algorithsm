N = int(input())

for i in range(1,N+1):
    print(' ' * (N-i) + '*' * i)

cnt = N-1
for i in range(1,N):
    print(' ' * i + '*' * cnt)
    cnt -= 1