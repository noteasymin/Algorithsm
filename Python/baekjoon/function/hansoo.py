import sys
import math
def hansoo():
    check_num = int(sys.stdin.readline())
    cnt = 0
    for i in range(1,int(check_num)+1):
        if i < 10:
            cnt += 1
        elif i < 100:
            cnt += 1
        elif i < 1000:
            fnum = (math.floor(i/100) % 10)
            snum = (math.floor(i/10) % 10)
            tnum = (i%10)
            d1 = tnum - snum
            d2 = snum - fnum
            if d1 == d2:
                cnt += 1
        
    print(cnt)
        
hansoo()