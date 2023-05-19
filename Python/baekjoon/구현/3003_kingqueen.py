def solution():
    lst = [1, 1, 2, 2, 2, 8]
    
    lst2 = list(map(int,input().split()))
    print(lst2)
    for i in range(6):
        lst[i] = lst[i] - lst2[i]
    
    for i in range(6):
        print(lst[i],end=" ")
solution()