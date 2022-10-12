import sys
def sum():
    cnt = int(sys.stdin.readline())
    num = sys.stdin.readline().strip()
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)
sum()