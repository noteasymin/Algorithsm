import sys

def age():
    n = int(sys.stdin.readline())
    lst = dict()
    for i in range(n):
        key_value = sys.stdin.readline().split()
        lst[key_value[1]]=int(key_value[0])
    
    lst = sorted(lst.items(),key=lambda x : x[1])

    for i in lst:
        print(i[1],i[0])

age()