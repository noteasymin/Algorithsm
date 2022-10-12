def quiz():
    score = 0
    answer = input()
    score_of_o = 1
    for i in answer:
        if i == "O":
            score += score_of_o
            score_of_o += 1
        else:
            score_of_o = 1
    print(score)

cnt = int(input())
for i in range(cnt):
    quiz()

