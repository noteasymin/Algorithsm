import sys
T = int(sys.stdin.readline())

for i in range(1,T+1):
    num1, num2 = map(int,sys.stdin.readline().split())
    print("Case #{0}:".format(i),num1 + num2)