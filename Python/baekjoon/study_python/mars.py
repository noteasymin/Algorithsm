def mars():

    TC = int(input())

    for i in range(TC):
        sentence = input().split(" ")
        num = float(sentence[0])
        del sentence[0]
        for j in sentence:
            if j == '@':
                num *= 3
            elif j == '%':
                num += 5
            elif j == '#':
                num -= 7
        print("{:.2f}".format(num))

mars()