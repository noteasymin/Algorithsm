import sys

k, p, n = list(map(int, sys.stdin.readline()))

for i in range(n):
    k = (k * p) % 1000000007

print(k)