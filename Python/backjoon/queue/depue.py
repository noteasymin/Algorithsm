import sys
from collections import deque

def push_front(v):
    global queue
    v = int(v)
    queue.appendleft(v)

def push_back(v):
    global queue
    v = int(v)
    queue.append(v)

def pop_front():
    global queue
    if len(queue) == 0:
        print(-1)
    else:
        a = queue.popleft()
        print(a)

def pop_back():
    global queue
    if len(queue) == 0:
        print(-1)
    else:
        a = queue.pop()
        print(a)

def size():
    global queue
    print(len(queue))

def empty():
    global queue
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    global queue
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    global queue
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[len(queue)-1])

queue = deque()
command_sen = []

N = int(sys.stdin.readline())

for _ in range(N):
    command_sen = list(map(str,sys.stdin.readline().split()))
    
    if command_sen[0] == 'push_front':
        push_front(command_sen[1])
    
    elif command_sen[0] == 'push_back':
        push_back(command_sen[1])
    
    elif command_sen[0] == 'pop_front':
        pop_front()

    elif command_sen[0] == 'pop_back':
        pop_back()

    elif command_sen[0] == 'size':
        size()

    elif command_sen[0] == 'empty':
        empty()

    elif command_sen[0] == 'front':
        front()

    elif command_sen[0] == 'back':
        back()
    
