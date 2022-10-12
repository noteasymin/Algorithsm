from ntpath import join


def sort():
    word = input()
    word = sorted(word)
    new_word = []
    sum = 0

    for i in range(len(word)):

        if ord(word[i]) >= 48 and ord(word[i]) <= 57:
            sum += int(word[i])

        else:
            new_word.append(word[i])    
            

            
    new_word = "".join(new_word)
    print(new_word + str(sum))

sort()