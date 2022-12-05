M = int(input())
N = int(input())

graph = [False,False] + [True] * (2*N)
primes = []

for i in range(2, N * 2):
    if graph[i]:
        primes.append(i)
        for j in range(2*i, N*2, i):
            graph[j] = False

for i in primes:
    if i >= M:
        min_M = i
        cnt = primes.index(i)
        break

for i in primes:
    if i >= min_M and N < i:
        max_N = i
        cnt2 = primes.index(i)
        break
temp = 0
for i in primes:
    if M <= i <= N:
        temp = i
        break
if temp == 0:
    print(-1)
else:
    print(sum(primes[cnt:cnt2]))
    print(min_M)