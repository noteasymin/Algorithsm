import sys


N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
result = 0
cnt = 0
lst = sorted(lst)


for _ in range(N):
    result += sum(lst[:cnt+1])
    print(result)
    cnt += 1
print(result)
