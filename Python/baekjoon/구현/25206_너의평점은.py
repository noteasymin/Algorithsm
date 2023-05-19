def solution():
    cnt = 0
    sum_of_score = 0
    dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
    for _ in range(20):
        subject, score, grade = map(str, input().split())

        if grade == 'P':
            continue
        else:
            sum_of_score += float(score) * dic[grade]
            cnt += float(score)

    print((sum_of_score / cnt).__round__(6))


solution()
