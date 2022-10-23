n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8:)