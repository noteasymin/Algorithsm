def sum():
    num = int(input())
    cnt = 1
    sum = 0
    while True:
        if sum >= num:
            break

        else:
            cnt += 1
            sum += cnt

    if num == 2:
        print(1)
    else:
        print(cnt - 1)

sum()