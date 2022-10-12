import sys


#def dfs():

#def bfs():


N, M, V = map(int,sys.stdin.readline().split())

lst = [[0] for i in range(N)]
print(lst)

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    lst[a].append(b)

print(lst)


