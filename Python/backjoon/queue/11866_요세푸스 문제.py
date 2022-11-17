import sys
from collections import deque
N, K = map(int, input().split())

lst = [i for i in range(1,N+1)]
queue = deque(lst)
res = []
i = 0

while queue:
    i += 1
    tmp = queue.popleft()
    if i % K != 0:
        queue.append(tmp)
    else:
        res.append(tmp)


s = ', '.join(map(str, res))
print('<' + s + '>')