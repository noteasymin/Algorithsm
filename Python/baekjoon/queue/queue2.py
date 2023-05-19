from collections import deque
import sys
def queue():
    cnt = int(sys.stdin.readline())
    q2 = deque()
    for i in range(cnt):
        word = []
        word = sys.stdin.readline().split()
        if word[0] == 'push':
            q2.append(word[1])
        
        elif word[0] =='pop':
            if len(q2) == 0:
                print(-1)
            else:
                print(q2[0])
                del q2[0]
        elif word[0] =='size':
            print(len(q2))

        elif word[0] =='empty':
            if len(q2) == 0:
                print(1)
            else:
                print(0)
        elif word[0] =='front':
            if len(q2) == 0:
                print(-1)
            else:
                print(q2[0])
        elif word[0] =='back':
            if len(q2) == 0:
                print(-1)
            else:
                print(q2[-1])

queue()
