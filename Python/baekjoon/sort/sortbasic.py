def sort():
    N = int(input())
    
    lst = list(map(int,input().split(" ")))
    lst = set(lst)
    lst = sorted(lst)
    
    for i in lst:
        print(i,end=" ")
    
sort()