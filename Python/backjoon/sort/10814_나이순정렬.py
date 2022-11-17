import sys
def solution():
    input = sys.stdin.readline
    n = int(input())
    arr = []
    for i in range(n):
        info = input()
        arr.append(info.rstrip())


    arr2 = sorted(arr,key = lambda x : int(x.split(' ')[0]))

    for i in arr2:
        print(i)
solution()