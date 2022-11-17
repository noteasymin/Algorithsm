from collections import deque
import sys

def card():
    
    cnt = int(sys.stdin.readline())
    c = deque(i+1 for i in range(cnt))

    for i in range(cnt - 1):
        del c[0]

        c.append(c[0])

        del c[0]

    print(c[0])
        
card()