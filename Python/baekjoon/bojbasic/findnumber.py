import sys

input = sys.stdin.readline
def find():
    N = int(input())

    lst = list(map(int,input().split(" ")))

    M = int(input())

    findlst = list(map(int,input().split(" ")))

    for i in findlst:
        if i in lst:
            print("1")
        else:
            print('0')

find()