def solution():
    lst = ['c=','c-','d-','lj','nj','s=','z=','dz=']


    sentence = input()
    cnt = 0
    cnt2 = 0

    while len(sentence) > 0:
        if sentence[0:3] == 'dz=':
            cnt += 1
            sentence = sentence[3:]
        elif sentence[0:2] in lst:
            cnt += 1
            sentence = sentence[2:]
        else:
            cnt2 += 1
            sentence = sentence[1:]

    cnt = cnt + cnt2
    print(cnt)
solution()