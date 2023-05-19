import sys

def solution():
    input = sys.stdin.readline
    x,y,z = 1, 1, 1

    while True:
        x, y, z = map(int,input().split())

        if x == 0 and y == 0 and z == 0:
            break
        elif x == 1 and y == 1 and z == 1:
            print('wrong')

        if x ** 2 + y ** 2 == z ** 2:
            print('right')
        elif x ** 2 == y ** 2 + z ** 2:
            print('right')
        elif x ** 2 + z ** 2 == y ** 2:
            print('right')
        else:
            print('wrong')

solution()