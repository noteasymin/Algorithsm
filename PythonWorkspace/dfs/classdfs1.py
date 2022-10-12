def dfs(graph, R, visited):
    visited[R] = True

    for i in graph[R]:
        if visited[i] == True:



def solution():
    N, M, R = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N + 1)
    print(visited)

    for i in range(M):
        u, v = map(int,input().split())

        graph[u].append(v)
        graph[v].append(u)

    for i in range(N+1):
        graph[i].sort()

    dfs(graph, R, visited)

solution()