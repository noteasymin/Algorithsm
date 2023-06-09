def recursive(array, start, now_length):
    temp = now_length // 3

    if temp == 0:
        return

    for i in range(start + temp, start + temp * 2):
        array[i] = ' '

    recursive(array, start, temp)
    recursive(array, start + temp * 2, temp)


def solution():
    while True:
        try:
            n = input()
            if n == '':
                break
            else:
                n = int(n)
                array = ['-' for i in range(pow(3, n))]
                recursive(array, 0, pow(3, n))
                answer = ''
                for i in array:
                    answer += i
                print(answer)

        except EOFError:
            break


solution()
