def solution(s):
    answer = 0
    sentence = []
    idx = 0
    while s:
        if s[idx] == 'z':
            sentence.append(0)
            for i in range(4):
                del s[0]
        elif s[idx] == 'o':
            sentence.append(1)
            for i in range(3):
                del s[0]
        elif s[idx] == 't':
            if s[idx+1] =='w':
                sentence.append(2)
                for i in range(3):
                    del s[0]
            else:
                sentence.append(3)
                for i in range(5):
                    del s[0]
        elif s[idx] == 'f':
            if s[idx+1] =='o':
                sentence.append(4)
            else:
                sentence.append(5)
            for i in range(4):
                del s[0]
        elif s[idx] == 's':
            if s[idx+1] =='i':
                sentence.append(6)
                for i in range(3):
                    del s[0]
            else:
                sentence.append(7)
                for i in range(5):
                    del s[0]
        elif s[idx] == 'e':
            sentence.append(8)
            for i in range(5):
                del s[0]
        elif s[idx] == 'n':
            sentence.append(9)
            for i in range(4):
                del s[0]
        else:
            sentence.append(s[idx])
            del s[0]
        
    
    print(sentence)
    return answer

solution('one')