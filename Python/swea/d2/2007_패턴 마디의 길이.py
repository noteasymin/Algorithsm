def solution():
    T = int(input())
    for tc in range(1, T + 1):
        string = input()
        for i in range(1, 11):
            if string[:i] == string[i:i * 2]:
                print('#{} {}'.format(tc, i))
                break


solution()
