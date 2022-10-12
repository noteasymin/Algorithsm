def solution(levels):
    num_lst = []
    levels.sort()
    cnt = len(levels)// 4

    for i in range(1,cnt+1):
        num_lst.append(levels[-i])


    print(min(num_lst))

levels = [1,2,3,4,5,6,7,8,9]
solution(levels)