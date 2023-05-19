def decom():
    number = int(input())
    c = len(str(number))

    if number-c*9 <= 0:
        if number % 2 == 0:
            print(number // 2)
        else:
            print(0)
        return 0

    for i in range(number-c*9,number):
        if i < 10:
            continue

        result = 0 + i
        new_n = 0 + i
        n = list(str(i))

        for j in range(len(n)):
            new_n += int(n[j])

        if new_n == number:
            print(result)
            return 0
    print(0)

decom()
