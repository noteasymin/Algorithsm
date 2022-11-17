import math
N = int(input())

N = math.factorial(N)

N = str(N)

N = list(N)

N = list(reversed(N))

cnt = 0

for i in N:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)