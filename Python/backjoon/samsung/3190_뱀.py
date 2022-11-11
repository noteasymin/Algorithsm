from collections import deque
N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for i in range(N)]


for i in range(K):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

graph[0][0] = 2
direction = ['E','S','W','N']
loc = 0
L = int(input())
command_lst = deque()

for i in range(L):
    command = input().split()
    command_lst.append(command)

print(command_lst)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0

while True:
    time += 1
    if int(command_lst[0][0]) == time and len(command_lst) > 0:
        if command_lst[0][1] == 'D':
            loc += 1
            loc %= 4
        else:
            loc -= 1
            loc %= 4
        command_lst.popleft()
    print(loc)
