import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [0] * (N + 1)
answer = [0] * N
cnt = 1

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)


def dfs(R):
    global cnt
    visited[R] = 1
    answer[R - 1] = cnt
    cnt += 1

    for i in graph[R]:
        if visited[i]:
            continue
        dfs(i)


dfs(R)

for i in answer:
    print(i)
