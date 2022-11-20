T = int(input())
result = []
for i in range(1,T+1):
    N, S = map(int, input().split())
    graph = list(map(int, input().split()))
    answer = 0
    graph = sorted(graph)
    for _ in range(N):
        temp = []
        for j in graph:
            temp.append(abs(S-j))


        S = graph[temp.index(min(temp))]
        graph.remove(S)
        answer += min(temp)


    print(f'#{i} {answer}')

