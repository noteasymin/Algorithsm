def croatia():
    c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    sentence = input()
    cnt = 0

    for i in c_alphabet:
        if i in sentence:
                cnt += 1
                sentence = sentence.replace(i,"",1)
                c_alphabet.remove(i)
                c_alphabet.append(i)    


    cnt += len(sentence)
    print(cnt)


croatia()