from collections import deque

gear = [deque(map(int, input())) for i in range(4)]
K = int(input())
seq = [[[], [2, 3, 4]], [[1], [3, 4]], [[2, 1], [4]], [[3, 2, 1], []]]


def rotate(g):
    g.appendleft(g.pop())


def rotate_reverse(g):
    g.append(g.popleft())


for i in range(K):
    gear_num, c = map(int, input().split())
    r = c
    gear_num -= 1
    lr_list = []
    lrr_list = []
    rr_list = []
    rrr_list = []
    if r == 1:
        lr_list.append(gear_num)
    else:
        lrr_list.append(gear_num)
    for i in seq[gear_num][0]:
        if gear[i][6] == gear[i - 1][2]:
            break
        else:
            if r == -1:
                lr_list.append(i - 1)
            else:
                lrr_list.append(i - 1)
            r *= -1
    # print(lr_list, lrr_list)
    r = c

    for i in seq[gear_num][1]:
        if gear[i - 2][2] == gear[i - 1][6]:
            break
        else:
            if r == -1:
                rr_list.append(i - 1)
            else:
                rrr_list.append(i - 1)
            r *= -1
    # print(rr_list, rrr_list)
    # print(gear)
    for i in lr_list:
        rotate(gear[i])
    for i in lrr_list:
        rotate_reverse(gear[i])
    for i in rr_list:
        rotate(gear[i])
    for i in rrr_list:
        rotate_reverse(gear[i])
    # print(gear)

answer = 0
idx = 0
for i in gear:
    if i[0] == 1:
        answer += 2 ** idx
    idx += 1
print(answer)
