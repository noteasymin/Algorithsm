import sys

N, M = map(int, sys.stdin.readline().split())
cnt = 0
S = set()
for i in range(N):
    S.add(sys.stdin.readline().strip())

str_lst = []
for i in range(M):
    str_lst.append(sys.stdin.readline().strip())


for i in str_lst:
    if i in S:
        cnt += 1

print(cnt)