def solution(strings, n):
    strings = sorted(strings)
    strings.sort(key = lambda x:x[n])
    print(strings)
    return strings

solution(["sun","bed","car"],1)