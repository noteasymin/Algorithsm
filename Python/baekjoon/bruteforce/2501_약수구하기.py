N, K = map(int, input().split())
cnt = 1
for i in range(1,N+1):
    if N % i == 0:
        if cnt == K:
            print(i)
            break
        cnt += 1
    if i == N:
        print(0)
        break
