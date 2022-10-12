import sys

originalList = []
list2 = []
list3 = []

N,X = map(int,sys.stdin.readline().split())

originalList = sys.stdin.readline().split()
list2 = list(map(int,originalList))

for i in range(0,N):
    if(list2[i] < X):
        list3.append(list2[i])

print(*list3)