S = input()
answer = []
for i in range(len(S)+1):
    for j in range(len(S)+1):
        answer.append(S[i:j])


print(len(set(answer)))