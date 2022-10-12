cnt = 0
def count():
    global cnt
    new_cnt = 0
    sentence = list(map(str,input()))
    while True:
        if len(sentence) == 0:
            break
        if sentence[0] == 'f' and sentence[1] == 'o' and sentence[2] == 'r':
            new_cnt += 1
            del sentence[0]
            del sentence[0]
            del sentence[0]
        elif sentence[0] == 'w' and sentence[1] == 'h' and sentence[2] == 'i' and sentence[3] == 'l' and sentence[4] == 'e':
            new_cnt += 1
            del sentence[0]
            del sentence[0]
            del sentence[0]
            del sentence[0]
            del sentence[0]
        else:
            del sentence[0]
    if cnt < new_cnt:
        cnt = new_cnt
    

n = int(input())
for i in range(n):
    count()

print(cnt)