import sys

X = int(sys.stdin.readline())
cnt = 0

while X != 1:
    if X % 3 == 0:
        X = X // 3

    elif X % 2 == 0:
        X = X // 2

    else:
        X -= 1
    
    cnt += 1
print(cnt)