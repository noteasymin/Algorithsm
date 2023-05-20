def solution():
    T = int(input())

    for i in range(1, T + 1):
        graph = []
        answer = []
        n, m = map(int, input().split())
        for j in range(n):
            graph.append(list(map(int, input().split())))
        fly(graph, n, m, answer)
        print(f'#{i} {max(answer)}')


def fly(graph, n, m, answer):
    # 파리채를 내려칠 곳 탐색
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flies = 0
            # 해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색
            for k in range(m):
                for l in range(m):
                    flies += graph[i+k][j+l]
            answer.append(flies)


solution()
