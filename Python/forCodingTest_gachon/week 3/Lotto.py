import copy


def solution(lottos, win_nums):
    cnt = 0
    result = []
    rank = [6,6,5,4,3,2,1]
    win_lottos = copy.deepcopy(lottos)
    lose_lottos = copy.deepcopy(lottos)

    print(win_lottos,lose_lottos)
    for i in range(len(lottos)):
        if win_lottos[i] == 0:
            win_lottos[i] = win_nums[0]

        if win_lottos[i] in win_nums:
            cnt += 1
            print('yes')
        else:
            print('no')
    result.append(rank[cnt])

    cnt = 0

    for i in range(len(lottos)):
        if lose_lottos[i] == 0:
            lose_lottos[i] = 46

        if lose_lottos[i] in win_nums:
            print('yes')
            cnt += 1
        else:
            print('no')
    result.append(rank[cnt])

    print(result)

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
solution(lottos,win_nums)