import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cnt = 0

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)