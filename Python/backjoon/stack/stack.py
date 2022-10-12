import sys
def stack():
    cnt = int(sys.stdin.readline())
    st = []


    for i in range(cnt):
        word = []
        word.append(sys.stdin.readline().split())
        if word[0][0] == 'push':
            push(st,int(word[0][1]))
        elif word[0][0] == 'pop':
            if len(st) == 0:
                print(-1)
            else:
                pop(st)
        elif word[0][0] =='size':
            size(st)
        elif word[0][0] == 'empty':
            empty(st)
        elif word[0][0] == 'top':
            top(st)
        
        
def push(lst,num):
    lst.append(num)

def pop(lst):
    print(lst[-1])
    del lst[-1]
        
def size(lst):
    print(len(lst))

def empty(lst):
    if len(lst) == 0:
        print(1)
    else:
        print(0)

def top(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])   
stack()