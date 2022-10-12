def sort2():
    cnt = int(input())
    num_list = []
    for i in range(cnt):
        num_list.append(int(input()))
    
    num_list = sorted(num_list,reverse = False)

    for i in range(cnt):
        print(num_list[i])

sort2()