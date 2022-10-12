groupword = 0
def solution():
    global groupword
    sentence = input()
    cnt = 0
    alphabet_lst = []

    for i in range(len(sentence)-1):
        if sentence[i] != sentence[i+1]:
            newword = sentence[i+1:]
            print(newword)
            if newword.count(sentence[i]) > 0:
                cnt += 1
    if cnt == 0:
        groupword += 1

index = int(input())
for i in range(index):
    solution()
print(groupword)