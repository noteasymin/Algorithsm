from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(sx,sy,ax,ay):
    q = deque()
    q.append([sx,sy])
    s[sx][sy] = 1

    while q:
        a,b = q.



t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int,input().split())
    ax, ay = map(int,input().split())

    s = [[0]*n for i in range(n)]
    bfs(sx,sy,ax,ay)

