import sys

N = int(sys.stdin.readline())
T = []
P = []

for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])
print(T,P)