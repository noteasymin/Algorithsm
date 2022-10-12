def group_word():
    cnt = int(input())
    word = []
    for i in range(cnt):
        word.append(input())
    
    check = []
    for i in range(len(word)):
        if word[i] not in check:
            check.append(word[i])



group_word()
