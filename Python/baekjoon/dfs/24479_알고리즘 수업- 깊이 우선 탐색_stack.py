import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):
    adj[i] = sorted(adj[i], reverse = True)

visited = [0] * (N+1)
nodes_cnt = [0] * (N+1)

order = 1

stack = deque()
stack.append(R)

while stack:
    cur_node = stack.pop()
    visited[cur_node] = 1

    if nodes_cnt[cur_node] == 0:
        nodes_cnt[cur_node] = order
        order += 1

    for next_node in adj[cur_node]:
        if visited[next_node] == 0:
            stack.append(next_node)

print(*nodes_cnt[1:])