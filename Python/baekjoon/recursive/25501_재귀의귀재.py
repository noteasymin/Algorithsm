import sys
cnt = 1

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        print(1, cnt)
        cnt = 0

    elif s[l] != s[r]:
        print(0, cnt)
        cnt = 0

    else:
        return recursion(s, l+1, r-1)

def isPalindrome(sentence):
    return recursion(sentence, 0, len(sentence)-1)

def solution():
    global cnt
    input = sys.stdin.readline

    T = int(input())
    cnt = 0

    for _ in range(T):
        sentence = input().rstrip()
        isPalindrome(sentence)




solution()