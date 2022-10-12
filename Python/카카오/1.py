import datetime
def solution(today, terms, privacies):
    answer = []
    cnt = 1
    today = datetime.datetime(int(today[0:4]),int(today[5:7]),int(today[8:10]))


    for i in privacies:
        newPrivacies = []
        newPrivacies.append(int(i[0:4]))
        newPrivacies.append(int(i[5:7]))
        newPrivacies.append(int(i[8:10]))

        for j in terms:
            if i[11] == j[0]:
                newPrivacies[1] += int(j[1:])
                break

        while True:
            if newPrivacies[1] > 12:
                newPrivacies[0] += 1
                newPrivacies[1] -= 12
                continue
            break
        time = datetime.datetime(newPrivacies[0],newPrivacies[1],newPrivacies[2])
        if time <= today:
            answer.append(cnt)
        cnt += 1
    return answer









today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
solution(today, terms, privacies)