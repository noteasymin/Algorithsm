import math
def ave():
    score = []
    for i in range(5):
        i = int(input())
        if i <= 40:
            score.append(40)
        else:
            score.append(i)
    total = sum(score)
    total = total / 5
    print(math.floor(total))

ave()