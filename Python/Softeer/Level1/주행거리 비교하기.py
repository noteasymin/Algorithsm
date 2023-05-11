import sys
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())

    if a > b:
        print('A')
    elif a < b:
        print('B')
    else:
        print('same')


solution()
