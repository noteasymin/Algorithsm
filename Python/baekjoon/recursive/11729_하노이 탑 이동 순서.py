def move(n, start, end):

    if n == 1:
        print(f'{start} {end}')
        return

    if n == 2:
        move()
def solution():
    n = int(input())

    move()