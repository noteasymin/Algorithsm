N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

for i in range(M):
    B.append(list(map(int, input().split())))


C = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for m in range(M):
            C[i][j] += A[i][m] * B[m][j]


for i in C:
    for j in i:
        print(j, end = ' ')
    print()