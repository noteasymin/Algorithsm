import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
sum = A * B * C
cnt = 0

sumstr = str(sum)
for i in range(0,10):
    print(sumstr.count(str(i)))