def sum(num):
    i = 1
    sum = 0
    ya = []
    
    while True:
        if num/2 < i:
            break

        if num % i == 0:
            sum += i
            ya.append(i)
        i += 1

    ya = map(str,ya)
    ya = ' + '.join(ya)
    if sum == num:
        print(f'{num} = {ya}')
    else:
        print(f'{num} is NOT perfect.')

while True:
    exit = int(input())

    if exit == -1:
        break
    else:
        sum(exit)