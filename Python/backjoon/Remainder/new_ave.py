def new_ave():
    cnt = int(input())
    new_score = []
    new_average = 0
    score_list = list(map(int, input().split()))
    max_score = max(score_list)
    
    for i in range(cnt):
        new_score.append(score_list[i]/max_score*100)
    
    for i in range(cnt):
        new_average += new_score[i]

    new_average /= cnt
    print(new_average)
        





new_ave()