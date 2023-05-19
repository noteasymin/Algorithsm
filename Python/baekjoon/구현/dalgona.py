def stick(board):
    l,d,x,y = map(int,input().split())
    x = x - 1
    y = y - 1
    if d == 0:
        for i in range(l):
            board[x][y+i] = 1
    else:
        for i in range(l):
            board[x+i][y] = 1

h, w = map(int,input().split())
n = int(input())

board = [[0 for j in range(w)] for i in range(h)]


for i in range(n):
    stick(board)

for i in range(h):
    for j in range(w):
        print(board[i][j],end =" ")
    print()