import sys
def coordinate():
    n = int(sys.stdin.readline())
    num_list = []

    for i in range(n):
        x,y = map(int,sys.stdin.readline().split())
        num_list.append([y,x])
    
    num_list = sorted(num_list)

    for y,x in num_list:
        print(x,y)
coordinate()