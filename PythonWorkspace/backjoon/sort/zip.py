import sys

def zip():
    n = int(sys.stdin.readline())
    num_list = list(map(int,sys.stdin.readline().split()))
    new_num_list = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            if num_list[i] > num_list[j]:
                cnt += 1
        new_num_list.append(cnt)

    
    print(new_num_list)

zip()