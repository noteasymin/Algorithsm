def solution(A, B):
    A.sort()
    B.sort()
    result = 0
    for i in range(len(A)):
        result += A[i] * B[-i - 1]

    return result
