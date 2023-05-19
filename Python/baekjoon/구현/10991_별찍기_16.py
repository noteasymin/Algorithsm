N = int(input())
cnt = N - 1
for i in range(1,N+1):
    print(' ' * cnt, end='')
    cnt -= 1
    print('* ' * i)
