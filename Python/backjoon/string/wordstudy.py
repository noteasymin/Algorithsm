from operator import index
import sys


def study():
    word = sys.stdin.readline().strip()
    word = word.lower()
    alphabet = []
    cnt = [0 for i in range(26)]

    for i in range(97,123):
        alphabet.append(chr(i))
       

    for i in word:
        if i in alphabet:
            j = alphabet.index(i)
            cnt[j] += 1
    
    max_alphabet = (max(cnt))
    max_alphabet_index = cnt.index(max(cnt))
    cnt.remove(max(cnt))
    smax_alphabet = max(cnt)
    

    if max_alphabet == smax_alphabet:
        print("?")
    else:
        answer = chr(max_alphabet_index + 97)
        print(answer.upper())
        


study()