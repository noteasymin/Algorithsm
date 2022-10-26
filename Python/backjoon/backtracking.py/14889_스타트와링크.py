import math
N = int(input())
lst = [i for i in range(1, N+1)]
graph = []
answer = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in lst:
    for j in lst:
        if i == j:
            continue

        temp = []
        for k in range(N):
            if lst[k] != i and lst[k] != j:
                temp.append(lst[k])
        a = temp[0]
        b = temp[1]

        answer.append(abs((graph[i-1][j-1] + graph[j-1][i-1]) - (graph[a-1][b-1] + graph[b-1][a-1])))

print(answer)
