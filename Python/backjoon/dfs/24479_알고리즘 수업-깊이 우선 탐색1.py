import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v)

    if visited.count(False) == 2:
        temp = visited.index(False,2)

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M, R = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N + 1)
temp = 0

for i in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

dfs(R)



if R not in graph[temp]:
    print(0)
else:
    print(R)