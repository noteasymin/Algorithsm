import sys

def solution():
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))

    arr2 = sorted(arr,reverse=True)

    print(arr2[m-1])
solution()