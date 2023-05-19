def shom():
    n = int(input())
    number = 1
    cnt = 0
    while True:
        if '666' in str(number):
            cnt += 1
            if cnt == n:
                print(number)
                break
            else:
                number += 1
            
        else:
            number += 1

shom()
