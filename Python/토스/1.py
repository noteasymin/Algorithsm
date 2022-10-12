def solution(s):
    cnt = 1
    num_lst = []

    for i in range(len(s)):
        if i == len(s)-1:
            if cnt == 3:
                num_lst.append(str(s[i - 1]) * 3)

            break
        if cnt == 3:
            num_lst.append(str(s[i-1]) * 3)

        if s[i] == s[i+1]:
            cnt += 1
            continue
        else:
            cnt = 1

    if len(num_lst) > 0:

        print(max(num_lst))

    else:
        print(-1)

s = '123'
solution(s)