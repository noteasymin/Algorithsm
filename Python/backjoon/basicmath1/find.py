from collections import deque


def find():
    num = int(input())
    cnt = 1
    num_list = deque()
    for i in range(10000000):
        if cnt not in num_list:
            num_list.append(cnt)
            cnt = 0
        else:
            num_list.append(cnt)
        cnt += 1
    print(num_list)


find()