import copy


def solution(s, times):
    if len(times) == 0:
        return [1,0]
    new_s = list(map(int,s.split(':')))
    cnt = 0
    day_lst = []
    flag = 1
    for i in times:
        i = list(map(int,i.split(':')))
        new_s[5] += i[3]
        new_s[4] += i[2]
        new_s[3] += i[1]
        new_s[2] += i[0]
        new_s.reverse()

        if new_s[0] >= 60:
            new_s[0] -= 60
            new_s[1] += 1

        if new_s[1] >= 60:
            new_s[1] -= 60
            new_s[2] += 1

        if new_s[2] >= 24:
            new_s[2] -= 24
            new_s[3] += 1

        if new_s[3] > 30:
            new_s[3] -= 30
            new_s[4] += 1

        if new_s[4] > 12:
            new_s[4] -= 12
            new_s[5] += 1
        new_s.reverse()
        temp = copy.deepcopy(new_s)
        day_lst.append(temp)

    for i in range(len(day_lst)):
        if cnt == 0:
            cnt += 1
            continue
        if day_lst[i][2] - day_lst[i-1][2] >= 2:
            flag = 0

        cnt += 1

    start = int(s[8:10])
    end = day_lst[-1][2]
    answer = 1
    print(start,end)
    while start != end:
        start += 1
        answer += 1
        if start > 30:
            start -= 30
        if start == end:
            break
    print(flag,answer)





s = "2021:04:12:16:08:35"
times = ['01:06:30:00',"01:01:12:00",'00:00:09:25']
solution(s, times)