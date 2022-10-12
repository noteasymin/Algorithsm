def score():
    num = input()
    if num != 'F':
        if num[0] == 'A':
            sc = 4
        elif num[0] == 'B':
            sc = 3
        elif num[0] == 'C':
            sc = 2
        else:
            sc = 1
        
        if num[1] == '+':
            sc += 0.3
        elif num[1] == '-':
            sc -= 0.3

        print("{:.1f}".format(sc))
    else:
        print(0.0)

score()
