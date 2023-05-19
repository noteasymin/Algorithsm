N = int(input())
cnt = N * 2
for i in range(1,N+1):
    print(('*' * i + ' ' * (cnt-i*2)).ljust(N*2,'*'))

cnt = 1
for i in range(N-1,0,-1):
    print(('*' * i +' ' * (cnt*2)).ljust(N*2,'*'))
    cnt += 1