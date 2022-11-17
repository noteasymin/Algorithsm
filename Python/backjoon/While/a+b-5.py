import sys

A = 1
while(A > 0):
    A, B = map(int,sys.stdin.readline().split())
    if(A == 0):
        break
    print(A+B) 