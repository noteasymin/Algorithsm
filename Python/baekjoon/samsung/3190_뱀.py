import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for i in range(N)]


for i in range(K):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
snake = deque([[0,0]])

graph[0][0] = 2
head = [0,0]
tail = [0,0]
loc = 0
L = int(input())
command_lst = deque()

for i in range(L):
    command = input().split()
    command_lst.append(command)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0

while True:
    time += 1


    nx = head[0] + dx[loc]
    ny = head[1] + dy[loc]

    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 2:
        if graph[nx][ny] == 0:
            head[0] = nx
            head[1] = ny
            snake.append([nx,ny])
            tail[0] = snake[0][0]
            tail[1] = snake[0][1]
            snake.popleft()
            graph[nx][ny] = 2
            graph[tail[0]][tail[1]] = 0
        elif graph[nx][ny] == 1:
            snake.append([nx, ny])
            graph[nx][ny] = 2
            head[0] = nx
            head[1] = ny
    elif nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == 2:
        print(time)
        break
    if len(command_lst) > 0 and int(command_lst[0][0]) == time:
        if command_lst[0][1] == 'D':
            loc += 1
            loc %= 4
        else:
            loc -= 1
            loc %= 4
        command_lst.popleft()
