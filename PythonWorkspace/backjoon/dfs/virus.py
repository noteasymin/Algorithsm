cnt = 0
def dfs(n):
    global cnt
    cnt += 1

    visitied[n] = True

    for i in graph[n]:
        if not visitied[i]:
            dfs(i)
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

visitied = [False] *(n+1)
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()


dfs(1)
print(cnt-1)