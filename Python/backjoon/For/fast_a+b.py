import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    num1, num2 = map(int,sys.stdin.readline().split())
    print(num1 + num2)