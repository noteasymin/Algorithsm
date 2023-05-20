def solution():
    t = int(input())

    for i in range(1, t + 1):
        word = input()

        reverse_word = "".join(list(reversed(word)))

        if word == reverse_word:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')


solution()
