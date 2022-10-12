import sys

try:
    while 1:
        A, B = map(int,sys.stdin.readline().split())
        print(A+B)
except:
    exit()
