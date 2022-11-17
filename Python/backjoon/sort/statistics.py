import sys
import math
from collections import Counter

def statitics():
    n = int(sys.stdin.readline())
    num_list = []

    for i in range(n):
        num_list.append(int(sys.stdin.readline()))
    num_list = sorted(num_list)

    ave = round(sum(num_list) / n)
    print(ave)

    if n % 2 == 0:
        cen = (num_list[math.floor(n/2)] + num_list[math.ceil(n/2)]) / 2
    else:
        cen = num_list[n//2]
    print(cen)

    mode = Counter(num_list)
    mode = mode.most_common()

    if n == 1:
        print(num_list[0])
    elif mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])

    print(max(num_list) - min(num_list))

    
    



statitics()