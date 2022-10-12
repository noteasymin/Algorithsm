import sys
input = sys.stdin.readline

def dfs(graph,V,visited):
    print(V,end=" ")
    visited[V] = 1

    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph,V,visited):
    pass


def solution():
    N, M, V = map(int,input().split())

    graph = [[] for i in range(N+1)]


    for i in range(M):
        v1, v2 = map(int,input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1,N+1):
        graph[i].sort()

    visited = [0] * (N+1)


    dfs(graph,V,visited)
    visited = [0] * (N + 1)
    bfs(graph,V,visited)

solution()