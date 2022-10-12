def soin():
    num = int(input())
    i = 2
    while True:
        if num % i == 0:
            num = num / i
            print(i)
        elif num < i:
            break
        else:
            i += 1
soin()
            