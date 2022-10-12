from collections import deque


def dfs(graph, V, visited):
    visited[V] = True
    print(V)
    for i in graph[V]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, V, visited):
    dq = deque()
    dq.append(V)
    visited[V] = True

    while dq:
        V = dq.popleft()
        for i in graph[V]:
            if not visited[i]:
                dq.append(V)
                visited[V] = True
                print(i)
j



def solution():
    N, M, V = map(int,input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for i in range(M):
        a, b = map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(M):
        graph[i].sort()

    dfs(graph, V, visited)
    visited = [False] * (N + 1)
    bfs(graph, V, visited)
solution()