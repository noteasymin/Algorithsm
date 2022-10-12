def their_average():
    students = 0
    students_and_score = input().split(" ")
    students_and_score = list(map(int,students_and_score))
    cnt = int(students_and_score[0])
    score_sum = 0

    for i in range(1,cnt + 1):
        score_sum += students_and_score[i]
    
    score_ave = score_sum / cnt

    for i in range(1,cnt + 1):
        if students_and_score[i] > score_ave:
            students += 1

    print("%.3f%%" % ((students/cnt)*100))
    

cnt = int(input())

for i in range(cnt):
    their_average()