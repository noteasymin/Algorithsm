import sys


def sort():
    n = int(sys.stdin.readline())
    word = []
    for i in range(n):
        word.append(sys.stdin.readline().strip())
    word = set(word)
    word = list(word)
    word.sort()
    word.sort(key=len)
    for i in word:
        print(i)

sort()
