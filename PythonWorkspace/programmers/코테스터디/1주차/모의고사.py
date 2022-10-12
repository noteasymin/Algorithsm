def solution(answers):
    first = [1, 2, 3, 4, 5] * 8
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    cnt = 0

    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0

    score_lst = []

    for i in range(len(answers)):
        if first[cnt] == answers[i]:
            cnt_1 += 1
        if second[cnt] == answers[i]:
            cnt_2 += 1
        if third[cnt] == answers[i]:
            cnt_3 += 1
    cnt += 1
    if cnt == 40:
        cnt = 0
    score_lst.append(cnt_1)
    score_lst.append(cnt_2)
    score_lst.append(cnt_3)

    max_num = max(score_lst)

    answer = []

    for i in range(len(score_lst)):
        if score_lst[i] == max_num:
            answer.append(i + 1)
    print(answer)

answers = [1,3,2,4,2]
solution(answers)