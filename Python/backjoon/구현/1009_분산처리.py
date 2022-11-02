import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = a
    for j in range(b-1):
        a = int(str(a)[-2:]) * c

    if a % 10 == 0:
        print(10)
    else:
        print(str(a)[-1])