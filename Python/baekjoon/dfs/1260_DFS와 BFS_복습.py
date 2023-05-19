import sys
from collections import deque
input = sys.stdin.readline

def dfs(a, graph, visited):
    print(a, end=' ')
    visited[a] = True

    for i in graph[a]:
        if not visited[i]:
            dfs(i, graph, visited)
def bfs(a, graph, visited):
    visited[a] = True
    queue = deque([a])

    while queue:
        num = queue.popleft()
        print(num, end = ' ')

        for i in graph[num]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(V, graph, visited)
visited = [False] * (N+1)
print()
bfs(V, graph, visited)