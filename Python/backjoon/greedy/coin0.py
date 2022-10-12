import sys
from collections import deque
def coin():
    n,k = map(int,sys.stdin.readline().split())
    s = deque()
    cnt = 0
    for i in range(n):
        s.append(int(sys.stdin.readline()))
    s.reverse()

    while True:
        if s[0] <= k :
            if k % s[0] == 0:
                cnt += k // s[0]
                k = s[0]*(k//s[0])
                continue
            else:
                k = k - s[0]
                cnt += 1
                continue
        else:
            s.popleft()
        if k == 0:
            break
    print(cnt)

coin()
