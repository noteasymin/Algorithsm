import sys

def repeat():
    word = input().split(" ")
    cnt = int(word[0])
    word = word[1]
    new_word = []
    for i in word:
        new_word.append(i*cnt)
    
    new_word = "".join(new_word)
    print(new_word)

cnt = int(sys.stdin.readline())

for i in range(cnt):
    repeat()