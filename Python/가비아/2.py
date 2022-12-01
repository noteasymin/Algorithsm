def solution(n):
    N = bin(n)[2:]
    answer = 0

    for i in range(len(N)):
        if int(N[i]) == 1:
            answer += 3 ** (len(N)-i-1)
    return answer

# https://claude-u.tistory.com/391