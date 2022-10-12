N = int(input())
T = N // 2

for i in range(1,T+1):
    if N % i == 0:
        print(i,end=' ')
print(N)