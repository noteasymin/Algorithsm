def solution():
    n = int(input())
    answer = 1

    if n != 0:
        answer = factorial(n, answer)

    print(answer)


def factorial(n, answer):
    if n == 1:
        return answer

    else:
        answer *= n
        n -= 1
        return factorial(n, answer)


solution()
