room = list(map(int, input()))

answer = 1
number = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 1, 8: 1, 9: 2}

for i in room:
    if i == 6 or i == 9:
        if number[9] > 0:
            number[9] -= 1
        else:
            for j in range(10):
                if j == i:
                    pass
                elif j == 6:
                    number[9] += 1
                else:
                    number[j] += 1
            answer += 1
    else:
        if number[i] > 0:
            number[i] -= 1
        else:
            for j in range(10):
                if j == i:
                    pass
                elif j == 6:
                    number[9] += 1
                else:
                    number[j] += 1
            answer += 1
print(answer)
