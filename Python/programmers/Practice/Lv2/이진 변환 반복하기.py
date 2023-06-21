def solution(s):
    s = str(s)
    zero = 0
    count = 0

    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    answer = [count, zero]
    return answer