while True:
    s = input()

    if s == 'END':
        break

    print(''.join(list(reversed(s))))