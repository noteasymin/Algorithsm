N = int(input())
graph = [[]] * N

for i in range(N):
    h = list(map(int, input().split()))
    graph[i] = h

print(graph)