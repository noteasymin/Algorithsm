def number_of_word():
    word = input().split(" ")

    if word[0] == "":
        del word[0]
    if word[-1] == "":
        del word[-1]
    
    print(len(word))
        


number_of_word()