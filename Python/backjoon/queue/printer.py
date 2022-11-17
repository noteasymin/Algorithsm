from collections import deque
import sys


def printer():
    N, M = map(int,sys.stdin.readline().split())
    priority = deque(map(int,sys.stdin.readline().split()))
    location = M
    cnt = 0
    if N == 1:
        print(1)
        return 0


    while True:
        if priority[0] == max(priority) and location == 0:
            print(cnt+1)
            priority.clear()
            return 0

        elif priority[0] == max(priority):
            priority.popleft()
            location -= 1
            if location < 0:
                location = len(priority)-1
            cnt += 1

        else:
            priority.append(priority[0])
            priority.popleft()
            location -= 1
            if location < 0:
                location = len(priority)-1





        
t = int(sys.stdin.readline())        
for i in range(t):
    printer()

