N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    K = (x2 - x1 + 1) * (y2 - y1 + 1)

    answer = 0

    for j in range(x1 - 1, x2):
        answer += sum(graph[j][y1 - 1:y2])

    print(answer)
