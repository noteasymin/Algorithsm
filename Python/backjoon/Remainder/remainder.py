remain_list =[]
new_list =[]
for i in range(10):
    remain_list.append(int(input())%42)
    if remain_list[i] in new_list:
        pass
    else:
        new_list.append(remain_list[i])

print(len(new_list))