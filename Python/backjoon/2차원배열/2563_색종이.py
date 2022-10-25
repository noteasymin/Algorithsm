N = int(input())
graph = [[0 for i in range(101)] for j in range(101)]

for i in range(N):
    a, b = map(int,input().split())

    for j in range(10):
        c = b
        for k in range(10):
            graph[a][c] = 1
            c += 1
        a += 1
cnt = 0
for i in graph:
    cnt += i.count(1)

print(cnt)