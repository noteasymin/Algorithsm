import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site = {}

for i in range(N):
    a, b = map(str, input().split())

    site[a] = b

for i in range(M):
    a = input().rstrip()

    print(site[a])