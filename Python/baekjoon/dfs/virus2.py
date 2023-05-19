import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    answer.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)




answer = []
def solution():
    n = int(input())
    s = int(input())

    graph = [[] for _ in range(n+1)]


    for i in range(s):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(graph)):
        graph[i].sort()



    visited = [False] * (n + 1)

    dfs(graph, 1, visited)
    print(len(answer) - 1)
solution()