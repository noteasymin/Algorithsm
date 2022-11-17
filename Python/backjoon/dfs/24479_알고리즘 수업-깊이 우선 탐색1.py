import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True
    answer[v] = cnt

    if visited.count(False) == 2:
        temp = visited.index(False,2)

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M, R = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N + 1)
temp = 0
answer = [[0] for i in range(N+1)]
cnt = 0
for i in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

dfs(R)

cnt = 0
for i in answer:
    if cnt == 0:
        cnt += 1
        continue
    if i ==[0]:
        print(0)
    else:
        print(i)
