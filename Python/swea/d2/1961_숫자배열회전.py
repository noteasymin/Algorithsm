def rotate(NN,N):
    new = [[0] * N for i in range(N)]
    print(new)

    for i in range(N):
        for j in range(N):
            new[j][N-i-1] = NN[i][j]
    print(new)
T = int(input())

for i in range(T):
    N = int(input())

    NN = []
    print(NN)
    for i in range(N):
        NN.append(list(map(int,input().split())))

    rotate(NN,N)

    print(NN)