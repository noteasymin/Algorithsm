from calendar import c


def pos():
    pos = 1
    block = ['>','>','<']
    cnt = 0
    print(block)
    while True:
        if block[pos] == '>':
            block[pos] = '<'
            pos += 1
            cnt += 1
        elif block[pos] == '<':
            block[pos] = '>'
            pos -= 1
            cnt += 1
        if pos < 0 or pos >= len(block):
            break
    print(cnt-1)

pos()